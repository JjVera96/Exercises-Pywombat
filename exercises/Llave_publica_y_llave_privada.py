# -*- coding: utf-8 -*-
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def get_public_and_private_key():
    keys = RSA.generate(1024)
    private_key = keys.export_key().decode('utf-8')
    public_key = keys.publickey().export_key().decode('utf-8')
    return private_key, public_key

private_key, public_key = get_public_and_private_key()
print('private_key: ', private_key)
print('public_key: ', public_key)

message = 'Hola mundo'
print('message: ', message)

key_encrypt = RSA.import_key(public_key)
cipher_encrypt = PKCS1_OAEP.new(key_encrypt)
encrypted_message = cipher_encrypt.encrypt(message.encode('utf-8'))
print('encrypted_message: ', encrypted_message)

key_decrypt = RSA.import_key(private_key)
cipher_decrypt = PKCS1_OAEP.new(key_decrypt)
decrypted_message = cipher_decrypt.decrypt(encrypted_message).decode('utf-8')
print('decrypted_message: ', decrypted_message)
