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

### Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

### License
MIT License
