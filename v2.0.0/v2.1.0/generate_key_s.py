from cryptography.fernet import Fernet
import os


#--------------------------------create key--------------------------------

def generate_key_symmetric():
    
    key = Fernet.generate_key() #creates the key
    with open('key_symmetric.key', 'wb') as key_file: # creates a file with the name key_symmetric.key and append permissions 'ab'
        # USAGE: open('file', 'mode'): -->  file: path and name of the file
        #                              -->  mode: 'a'(append, creates if not existing); 'w'(write, creates if not existing); 'r'(read, error if not existing); 'x'(create, error if existing)
        #                                         't'(text, default), 'b'(binary)
        key_file.write(key) # writes the key in the file
    

