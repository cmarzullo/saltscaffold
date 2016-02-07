
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'sets up files and directories for a new salt formula',
    'author': 'Christopher Marzullo',
    'url': 'https://bits.linode.com/cmarzullo/saltscaffold',
    'download_url': 'https://bits.linode.com/cmarzullo/saltscaffold/releases/latest',
    'author_email': 'cmarzullo@linode.com',
    'version': '2.0',
    'install_requires': ['nose','mako'],
    'packages': ['saltscaffold'],
    'scripts': [],
    'name': 'Saltscaffold',
    'entry_points': {
        'console_scripts': [
            'saltscaffold = saltscaffold.__main__:main',
        ]
    }

}

setup(**config)
