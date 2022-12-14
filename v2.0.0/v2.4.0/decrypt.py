from cryptography.fernet import Fernet
import os
#----------------------------------------------------------------------
from filter_files import define_useful_paths



#--------------------------------load key------------------------------
# we'll need the same key so the function to load it is the same
def load_key():
    return open('key_symmetric.key', 'rb').read()


#--------------------------------decryption------------------------------

def decrypt_process(paths_dic, key):  #(files to decrypt, key)
    fer = Fernet(key)  # using fernet method
    for path, files in paths_dic:
        for item in files:  # for every item on the directory
            with open(item, 'rb') as file:  # having opened the file in read binary mode,
                encrypted_data = file.read()   # save the data of the file in the variable
            decrypted_data = fer.decrypt(encrypted_data)  #decrypt the variable with fernet
            with open(item, 'wb') as file:  # then having the file opened anew in write binary mode,
                file.write(decrypted_data)  # rewrite the decrypted data 
# basically same that before but backwards

def decrypt():

    key = load_key()
    paths = define_useful_paths
    for p in paths:
        decrypt_process(p, key) #import from filter_files
