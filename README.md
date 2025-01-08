# Anon-Wallet 
## !IMPORTANT! 
### Send function is broken, you will not be able to send/withdraw bitcoin from your wallet until this is fixed. I have also had trouble importing the wallets generated from this tool into other wallet clients. I will be working on making things more modern and in compliance with standard practice. Until then, I do not recommend using this wallet.

- A Bitcoin wallet generator with AES-256 encryption.
- Compatible with desktop Linux, Termux for android and iSH for iOS. 
- Can generate, save & load multiple wallets. 
- Can be used as a cold storage wallet. 
- Can check balance and send Bitcoin using BlockCypher API token.

![IMG_0675](https://github.com/user-attachments/assets/6d0398f9-97f3-43b7-b6dd-e0e6d1dce315)

# Installation 
```
git clone https://github.com/cons0le7/Anon-Wallet/
cd ~/Anon-Wallet/installers
```

Select the appropriate Installer for your system.  

for desktop linux:
```
chmod +x install.sh 
./install.sh
```

for Termux: 
```
chmod +x termux.sh 
./install.sh
```

for iSH: 
```
chmod +x iSH.sh 
./iSH.sh
```

After installation:

```
cd ..
```


# Usage 

Run script: 

```
python3 start.py
```


You will be presented with 4 options upon running:

- Generate new wallet.
  - This will generate wallet Public and Private keys. You will have the option to show these keys in terminal, save to files without displaying or save and display. Be aware of your surroundings if you choose either option that displays keys, as private key should be kept private. 
    
- Encrypt wallet.
  - This will give the option to load keys from file or input keys manually thru terminal. if you choose to load from file, this will allow you to encrypt any wallet where keys are stored as 'public.txt' and 'private.txt' in the working directory (.../Anon-Wallet). This is the same format the keys are stored as during wallet generation. If you chose to have them saved as files during generation, you will be able to load them directly here.
  - Once keys are loaded or inputted, a decryption key will be generated and saved as 'decrypt.key' and the encrypted wallet will be stored as 'wallet.btc' You will then be prompted with a question asking if you would like to delete the plaintext keys. Unless you plan to back them up and store them somewhere else, it is recommended to do so as they will no longer be needed to open wallet.
  - You will be prompted to give a name for the directory in which the wallet will be saved. Both files 'wallet.btc' and 'decrypt.key' will be stored there. It is recommended to make corresponding folders for each of your wallets on a seperate storage device such as a flashdrive and move the keys there. Your wallet.btc will be inacessible without their key in the same directory. Take caution not to mix keys or wallets as they all have the same file names.
  - For further security you can create another set of corresponding folders on another seperate storage device. For example: you have 2 flash drives, both with the corresponding folders for your wallets, one set of folders on one flashdrive contains the wallet.btc files and the other contains the decrypt.key files. You can remove the files completely from your device and use them as cold storage wallets making them completely inaccessible in case of a compromised machine. To access again, you can transfer both files from your external drives into their corresponding folders in .../Anon-Wallet/.
  - After wallet is saved script will close. You will need to reload script with `python3 start.py`
 
- Open wallet.
  - This will list all saved wallets. You can choose which one to open. As long as both wallet.btc and decrypt.key are present in the wallets directory it will be decrypted and opened.
  - To access the wallet and check balance or sent Bitcoin, you will need to register with BlockCypher and aquire an auth token. this is free but be sure to look at their terms and conditions for details on usage and sending fees.
  - Register here:
    https://accounts.blockcypher.com/signup
  - Acquire token here:
    https://accounts.blockcypher.com/tokens
  - You can either copy the token, paste it into a text editor and save it as 'token.api' in '.../Anon-Wallet' (same directory as all the .py files.) or you can enter the token when prompted after choosing the option to open wallet and the script will automatically do this for you.
  - Keep your token private. You can also remove the token file and return it whenever you need to access your wallet for heightened security.
    
- Exit.
  - Close the script.
# Easy usage:
- First get a BlockCypher token:
  - Register here:
    https://accounts.blockcypher.com/signup
  - Acquire token here:
    https://accounts.blockcypher.com/tokens
    
- `python3 start.py` > Generate wallet (1) > Save to file (2) > Encrypt wallet (1) > Load keys from file (1) > yes > Enter wallet name > reload script `python3 start.py` > Open wallet > enter BlockCypher token. 
# Important Notes 
I made this for my own self Education. It is functional but I am not responsible for any financial losses that may occur from using this wallet. 

*I can not open your wallets if you lost the keys so do not ask.* 

Back up your wallets and your keys and keep them safe.

*Use at your own risk.*

  
