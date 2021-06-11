from stegano import lsb
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

def set_key(image_path, name, privkey_path):
    privkey = RSA.import_key(open(privkey_path, "rb").read())
    pubkey = privkey.publickey()
    signature = pkcs1_15.new(privkey).sign(SHA256.new(name.encode())).hex()
    img = lsb.hide(image_path, signature)
    img.save("signed.png")

def verify(image_path, name, pubkey_path):
    pubkey = RSA.import_key(open(pubkey_path, "rb").read())
    signature = lsb.reveal(image_path)
    signature = bytes.fromhex(signature)
    try:
        pkcs1_15.new(pubkey).verify(SHA256.new(name.encode()), signature)
    except:
        return False
    return True


