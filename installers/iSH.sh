#!/bin/bash

echo "Updating package list..."
apk update

echo "Installing Python and pip..."
apk add python3 py3-pip

echo "Installing required Python packages..."
pip3 install ecdsa requests base58

apk add py3-cryptography

echo "Verifying installation..."
python3 -c "import hashlib; import base58; import binascii; from ecdsa import SigningKey, SECP256k1; import json; import base64; import getpass; import requests; from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes; from cryptography.hazmat.backends import default_backend; from cryptography.hazmat.primitives import padding; import secrets"

if [ $? -eq 0 ]; then
    echo "All dependencies installed successfully."
else
    echo "There was an error in installation."
fi
