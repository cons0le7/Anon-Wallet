import sys
import os
import hashlib
import base58
import binascii
from ecdsa import SigningKey, SECP256k1

def generate_private_key():
    return os.urandom(32)

def private_key_to_public_key(private_key):
    sk = SigningKey.from_string(private_key, curve=SECP256k1)
    return sk.get_verifying_key().to_string()

def private_key_to_wif(private_key):
    versioned_key = b'\x80' + private_key
    hash1 = hashlib.sha256(versioned_key).digest()
    hash2 = hashlib.sha256(hash1).digest()
    checksum = hash2[:4]
    wif_key = versioned_key + checksum
    return base58.b58encode(wif_key)

def public_key_to_p2sh(public_key):
    sha256_hash = hashlib.sha256(public_key).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    versioned_hash = b'\x05' + ripemd160_hash
    hash1 = hashlib.sha256(versioned_hash).digest()
    hash2 = hashlib.sha256(hash1).digest()
    checksum = hash2[:4]
    p2sh_address = versioned_hash + checksum
    return base58.b58encode(p2sh_address)

def generate_wallet():
    private_key = generate_private_key()
    public_key = private_key_to_public_key(private_key)
    wif = private_key_to_wif(private_key)
    p2sh_address = public_key_to_p2sh(public_key)
    return {
        'private_key': private_key.hex(),
        'wif': wif.decode('utf-8'),
        'public_key': public_key.hex(),
        'p2sh_address': p2sh_address.decode('utf-8')
    }

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def generate():
    wallet = generate_wallet()
    display_option = input("\nGenerate public & private keys: \n\n(1) Display in terminal. \n(2) Save to file. \n(3) Save and display. \n(4) Back. \n\n")
    if display_option == '1' or display_option == '3':
        print("\nPrivate key: ", wallet['wif'])
        print("\nPublic key: ", wallet['p2sh_address'])
    if display_option == '2' or display_option == '3':
        save_to_file('private.txt', wallet['wif'])
        save_to_file('public.txt', wallet['p2sh_address'])
        print("\nKeys saved to private.txt and public.txt")
    elif display_option == '4':
        import reload_module
    encrypt_wallet = int(input("\n(1) Encrypt wallet. \n(2) Exit.\n\n"))
    try: 
        if encrypt_wallet == 1: 
            import encrypt_wallet
        elif encrypt_wallet == 2: 
            sys.exit()
        else: 
            print("\nInvalid input. Enter 1 or 2.") 
    except Exception as e: 
        print(f"\nAn error has occurred: {e}")
generate()