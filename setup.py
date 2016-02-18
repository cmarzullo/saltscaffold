
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'sets up files and directories for a new salt formula',
    'author': 'Christopher Marzullo',
    'url': 'https://github.com/cmarzullo/saltsaffold',
    'author_email': 'cmarzullo@linode.com',
    'version': '2.0',
    'install_requires': ['nose','mako'],
    'packages': ['saltscaffold'],
    'package_data': {
        '': [
            'skel/*.md',
            'skel/*.txt',
            'skel/*.sls',
            'skel/.gitignore',
            'skel/.kitchen.yml',
            'skel/.kitchen-ci.yml',
            'skel/formula/*.sls',
            'skel/formula/map.jinja',
            'skel/formula/defaults.yml',
            'skel/formula/files/config.conf',
            'skel/test/integration/default/serverspec/_spec.rb'
            ]
        },
    'scripts': [],
    'name': 'Saltscaffold',
    'entry_points': {
        'console_scripts': [
            'saltscaffold = saltscaffold.__main__:main',
            ]
        }
}

setup(**config)
