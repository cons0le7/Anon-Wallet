#!/bin/bash

echo "Reloading Anon-Wallet..."
dir=$(pwd)
processes=(
    "$dir/encrypt_wallet.py"
    "$dir/generate.py"
    "$dir/open_wallet.py"
    "$dir/save_wallet.py"
    "$dir/start.py"
)

check_running() {
    for process in "${processes[@]}"; do
        if pgrep -f "$process" > /dev/null; then
            return 0
        fi
    done
    return 1
}

for process in "${processes[@]}"; do
    pkill -f "$process"
done

while check_running; do
    sleep 0.5
done

python3 "$dir/start.py" 
