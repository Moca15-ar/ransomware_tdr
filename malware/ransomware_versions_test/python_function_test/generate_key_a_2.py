import rsa

# DOESNT WORK

def generate_keys():
    (publicKey, privateKey) = rsa.newkeys(2048)
    with open('publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def load_keys():
    with open('publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey

def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key) # rsa.encrypt(message, key).encode('ascii')

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

def sign(message, key):
    return rsa.sign(message.encode('ascii'), key, 'SHA-1')

def verify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key,) == 'SHA-1'
    except:
        return False

generate_keys()
publicKey, privateKey =load_keys()
print(publicKey)
print(privateKey)

message = input('Write your message here:')
ciphertext = encrypt(message, publicKey)
print(ciphertext)

text = decrypt(ciphertext, privateKey)
print(text)

print(f'Cipher text: {ciphertext}')

if text:
    print(f'Message text: {text}')
else:
    print(f'Unable to decrypt the message.')

