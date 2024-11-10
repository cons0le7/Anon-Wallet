import os
import json
import base64
import secrets
import getpass
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

BTC_FILE = 'wallet.btc'
KEY_SIZE = 32
BLOCK_SIZE = 16

def generate_decryption_key():
    return secrets.token_bytes(KEY_SIZE)

def save_key_to_file(key):
    with open('decrypt.key', 'wb') as key_file:
        key_file.write(key)

def encrypt(data, key):
    iv = os.urandom(BLOCK_SIZE)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()
    encryptor = cipher.encryptor()
    ct_bytes = encryptor.update(padded_data) + encryptor.finalize()
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    iv_b64 = base64.b64encode(iv).decode('utf-8')
    return json.dumps({'iv': iv_b64, 'ciphertext': ct})

def wallet():
    choice = input("\n(1) Load keys from file. \n(2) Enter keys manually. \n(3) Back. \n\n")
    
    if choice == '1':
        if os.path.exists('public.txt') and os.path.exists('private.txt'):
            with open('public.txt', 'r') as pub_file:
                public_key = pub_file.read().strip()
            with open('private.txt', 'r') as priv_file:
                private_key = priv_file.read().strip()
            print("\nKeys loaded successfully from files.")
        else:
            print("\nFile(s) not found. Please ensure 'public.txt' and 'private.txt' exist.")
            return
    elif choice == '2':
        public_key = input("\nEnter your BTC address public key: ")
        private_key = getpass.getpass("\nEnter your BTC address private key: ")
    elif choice == '3':
        import reload_module
    else:
        print("Invalid option. Exiting...")
        return

    decryption_key = generate_decryption_key()
    save_key_to_file(decryption_key)
    print("\nDecryption key saved as 'decrypt.key'. Keep this key securely stored away from the wallet.")
    print("\nEncrypting wallet...")
    encrypted_data = encrypt(f"{public_key},{private_key}", decryption_key)
    
    with open(BTC_FILE, 'w') as file:
        file.write(encrypted_data)
    print("\nWallet keys encrypted and saved successfully to 'wallet.btc'.")

    delete_keys = input("\nWould you like to delete the plaintext keys from the files? (yes/no): ")
    if delete_keys.lower() == 'yes':
        if os.path.exists('public.txt'):
            os.remove('public.txt')
        if os.path.exists('private.txt'):
            os.remove('private.txt')
        print("\nPlaintext keys deleted successfully.")
    
    import save_wallet 
        
wallet()