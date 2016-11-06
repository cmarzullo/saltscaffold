
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

config = {
    'description': 'sets up files and directories for a new salt formula',
    'long_description': read_md('README.md'),
    'author': 'Christopher Marzullo',
    'url': 'https://github.com/cmarzullo/saltsaffold',
    'author_email': 'cmarzullo@linode.com',
    'version': '3.0.5',
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
            'skel/Gemfile',
            'skel/formula/*.sls',
            'skel/formula/map.jinja',
            'skel/formula/defaults.yml',
            'skel/formula/files/config.conf',
            'skel/test/integration/default/serverspec/_spec.rb',
            'skel/test/mockup/*.sls'
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
