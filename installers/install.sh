#!/bin/bash

wallet_dir="$(dirname "$(pwd)")"
chmod +x "$wallet_dir/reload.sh"

echo "Updating package list..."
sudo apt-get update

echo "Installing Python and pip..."
sudo apt-get install -y python3 python3-pip

echo "Installing required Python packages..."
sudo apt install python3-ecdsa 
sudo apt install python3-cryptography 
sudo apt install python3-requests 
sudo apt install base58 -y 

echo "Verifying installation..."
sudo python3 -c "import hashlib; import base58; import binascii; from ecdsa import SigningKey, SECP256k1; import json; import base64; import getpass; import requests; from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes; from cryptography.hazmat.backends import default_backend; from cryptography.hazmat.primitives import padding; import secrets"

if [ $? -eq 0 ]; then
    echo "All dependencies installed successfully."
else
    echo "There was an error in installation."
fi
