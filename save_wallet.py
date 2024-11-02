import os
import shutil
import sys

def save():
    wallet_file = 'wallet.btc'
    key_file = 'decrypt.key'
    files_found = []

    if os.path.isfile(wallet_file):
        files_found.append(wallet_file)
    if os.path.isfile(key_file):
        files_found.append(key_file)

    if files_found:
        while True:
            folder_name = input("\nPlease enter a name for this wallet's folder: ").strip()
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                break
            else:
                print("Directory already exists. Please choose a different name.")

        for file in files_found:
            shutil.copy(file, folder_name)
        print("\nWallet saved successfully. \nScript must be reloaded to use.")
        print("\nExiting...")
        sys.exit()
save()