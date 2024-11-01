# Anon-Wallet 
- A Bitcoin wallet generator with AES-256 encryption.
- Compatible with desktop linux distros, Termux for android and iSH for iOS. 
- Can generate, save & load multiple wallets. 
- Can be used as a cold storage wallet. 
- Can check balance and send Bitcoin using BlockCypher token.

# Installation 
```
cd Anon-Wallet
cd installers
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
./install.sh`
```

for iSH: 
```
chmod +x iSH.sh 
./iSH.sh`
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
  - This will give the option to load keys from file or input keys manually thru terminal. if you choose to load from file, this will allow you to encrypt any wallet where keys are stored as 'public.txt' and 'private.txt' in the working directory (.../Anon-Wallet/). This is the same format the keys are stored as during wallet generation. If you chose to have them saved as files during generation, you will be able to load them directly here.
  - Once keys are loaded or inputted, a decryption key will be generated and saved as 'decrypt.key' and the encrypted wallet will be stored as 'wallet.btc' You will then be prompted with a question asking if you would like to delete the plaintext keys. Unless you plan to back them up and store them somewhere else, it is recommended to do so as they will no longer be needed to open wallet. 
 
- Open wallet.'
  
- Exit.

  
