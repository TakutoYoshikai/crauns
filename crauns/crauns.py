from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from lina import lina
import base64
import sys
import argparse
from PIL import Image

def set_key(image_path, name, privkey_path):
    privkey = RSA.import_key(open(privkey_path, "rb").read())
    pubkey = privkey.publickey()
    signature = pkcs1_15.new(privkey).sign(SHA256.new(name.encode()))
    img = Image.open(image_path)
    data = lina.hide(img, signature)
    data.save("signed.png")

def verify(image_path, name, pubkey_path):
    pubkey = RSA.import_key(open(pubkey_path, "rb").read())
    img = Image.open(image_path)
    signature = lina.reveal(img)
    try:
        pkcs1_15.new(pubkey).verify(SHA256.new(name.encode()), signature)
    except:
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description="crauns")
    parser.add_argument("mode", help="set or verify")
    parser.add_argument("-i", "--image", help="image")
    parser.add_argument("-n", "--name", help="name")
    parser.add_argument("-v", "--priv", help="private key")
    parser.add_argument("-p", "--pub", help="public key")
    args = vars(parser.parse_args())
    if args["mode"] == "set":
        set_key(args["image"], args["name"], args["priv"])
    elif args["mode"] == "verify":
        print(verify(args["image"], args["name"], args["pub"]))

if __name__ == "__main__":
    main()
