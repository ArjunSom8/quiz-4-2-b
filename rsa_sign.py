from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

passphrase = 'dees'

with open('private.pem', 'rb') as f:
    pkey = RSA.importKey(f.read(), passphrase=passphrase)
m = b'Hello world!'
hash = SHA256.new(m)
pk = PKCS1_v1_5.new(pkey)
signed_message = pk.sign(hash)
print(signed_message.hex())

