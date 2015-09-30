
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'sets up files and directories for a new salt formula',
    'author': 'Christopher Marzullo',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'cmarzullo@linode.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['saltscaffold'],
    'scripts': [],
    'name': 'Saltscaffold'
}

setup(**config)
