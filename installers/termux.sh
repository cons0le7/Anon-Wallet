#!/bin/bash

wallet_dir="$(dirname "$(pwd)")"
chmod +x "$wallet_dir/reload.sh"

echo "Updating package list..."
pkg update

echo "Installing Python and pip..."
pkg install -y python3 python-pip

echo "Installing required Python packages..."
pip3 install ecdsa requests
pkg install python-cryptography
python -m pip install base58

echo "Verifying installation..."
python3 -c "import hashlib; import base58; import binascii; from ecdsa import SigningKey, SECP256k1; import json; import base64; import getpass; import requests; from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes; from cryptography.hazmat.backends import default_backend; from cryptography.hazmat.primitives import padding; import secrets"

if [ $? -eq 0 ]; then
    echo "All dependencies installed successfully."
else
    echo "There was an error in installation."
fi
