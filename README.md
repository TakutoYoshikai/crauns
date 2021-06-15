# crauns
crauns is a tool to prove that the person is a member of the same group by scanning thumbnail icon. It uses RSA private key and public key to sign.

### Usage
**install**
```bash
pip install git+https://github.com/TakutoYoshikai/crauns.git
```

**sign**
```bash
crauns set -i <THUMBNAIL ICON> -n <YOUR ID OR NAME> -v <RSA PRIVATE KEY>
```

**verify**
```bash
crauns verify -i <THUMBNAIL ICON SIGNED> -n <YOUR ID OR NAME> -p <RSA PUBLIC KEY>
```

### License
MIT License
