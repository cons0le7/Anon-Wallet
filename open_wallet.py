import os
import json
import base64
import getpass
import requests
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

BTC_FILE = 'wallet.btc'
TOKEN_FILE = 'token.api'
KEY_SIZE = 32
BLOCK_SIZE = 16

def load_key_from_file(directory):
    key_path = os.path.join(directory, 'decrypt.key')
    if os.path.exists(key_path):
        with open(key_path, 'rb') as key_file:
            return key_file.read()
    else:
        return None

def decrypt(enc_data, key):
    b64 = json.loads(enc_data)
    iv = base64.b64decode(b64['iv'])
    ct = base64.b64decode(b64['ciphertext'])
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ct) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    pt = unpadder.update(padded_data) + unpadder.finalize()
    return pt.decode('utf-8')
    
def check_balance(public_key, token):
    url = f'https://api.blockcypher.com/v1/btc/main/addrs/{public_key}/balance?token={token}'
    response = requests.get(url)
    
    if response.status_code == 200:
        balance_info = response.json()
        balance = balance_info['final_balance'] / 1e8
        return f"\nBalance for {public_key}: {balance:.8f} BTC"
    else:
        return f"\nError fetching balance: {response.text}"
def send_bitcoin(private_key, to_address, amount, token):
    try:
        amount_in_satoshis = int(float(amount) * 1e8)
    except ValueError:
        return "\nError: Invalid amount format. Please enter a valid number."

    url = f'https://api.blockcypher.com/v1/btc/main/txs/new?token={token}'
    tx_data = {
        "inputs": [{"addresses": [private_key]}],
        "outputs": [{"addresses": [to_address], "value": amount_in_satoshis}]
    }
    
    response = requests.post(url, json=tx_data)
    if response.status_code == 201:
        tx_info = response.json()
        return f"\nTransaction created successfully. Transaction ID: {tx_info['tx']['hash']}"
    else:
        return f"\nError sending Bitcoin: {response.text}"

def get_blockcypher_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as file:
            return file.read().strip()
    else:
        token = input("Enter your BlockCypher API token: ")
        test_url = f'https://api.blockcypher.com/v1/btc/main?token={token}'
        response = requests.get(test_url)
        if response.status_code == 200:
            with open(TOKEN_FILE, 'w') as file:
                file.write(token)
            print("\nToken saved successfully as 'token.api'.")
            return token
        else:
            print("\nInvalid BlockCypher API token. Please try again.")
            return get_blockcypher_token()

def list_directories():
    directories = [d for d in os.listdir() if os.path.isdir(d) and d not in ('__pycache__', '.git', 'installers')]
    return directories

def wallet():
    blockcypher_token = get_blockcypher_token()
    directories = list_directories()
    selected_directory = None 
    public_key = None 
    private_key = None 

    if directories:
        print("\nWallet(s) found. Please select one:\n")
        for index, directory in enumerate(directories):
            print(f"({index + 1}) {directory}")
        choice = int(input("\nSelect a wallet by number: ")) - 1
        if choice < 0 or choice >= len(directories):
            print("\nInvalid selection.")
            return
        selected_directory = directories[choice]
    else:
        print("\nNo saved wallets found. Checking for unsaved wallet...")
        if os.path.exists(BTC_FILE) and os.path.exists('decrypt.key'):
            selected_directory = os.getcwd()
            print("\nUnsaved wallet found!")
        else:
            new_wallet = input("\nNo wallet found. Would you like to create one? (yes/no): ").strip().lower()
            if new_wallet == 'yes':
                import generate  
            elif new_wallet == 'no':
                print("\nExiting...")
                sys.exit()
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                return

    if selected_directory:
        btc_path = os.path.join(selected_directory, BTC_FILE)
        if os.path.exists(btc_path):
            try:
                with open(btc_path, 'r') as file:
                    encrypted_data = file.read()
                decryption_key = load_key_from_file(selected_directory) if selected_directory != os.getcwd() else load_key_from_file('.')
                print("\n'wallet.btc' and 'decrypt.key' loaded successfully.")
                print("\nDecrypting...")
                decrypted_data = decrypt(encrypted_data, decryption_key)
                public_key, private_key = decrypted_data.split(',')
                print("\nWallet opened successfully.")
            except Exception as e:
                print("\nFailed to decrypt the wallet:", str(e))
                return
        else:
            print("\nWallet file not found.")
            return

    while True:
        print("\n(1) Check Balance")
        print("(2) Send Bitcoin")
        print("(3) Main menu")
        print("(4) Exit")
        choice = input("\nChoose an option: ")
        if choice == '1':
            print(check_balance(public_key, blockcypher_token))
        elif choice == '2':
            to_address = input("\nEnter the recipient's address: ")
            amount = float(input("\nEnter the amount to send: "))
            print(send_bitcoin(private_key, to_address, amount, blockcypher_token))
        elif choice == '4':
            print("\nExiting...")
            break
        elif choice == '3': 
            import reload_module
        else:
            print("\nInvalid option. Please try again.")

wallet()