from setuptools import setup, find_packages

setup(
    name = 'crauns',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/crauns.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = 'crauns',
    install_requires = ['setuptools', "pycryptodome==3.14.1", "lina@git+https://github.com/TakutoYoshikai/lina.git"],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "crauns = crauns.crauns:main",
        ]
    }
)
