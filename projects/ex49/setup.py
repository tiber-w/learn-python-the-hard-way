try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
        'description': '',
        'author': 'Tiber Wang',
        'url': '',
        'download_url': ','
        'author_email': 'tiber_w@outlook.com'
        'version': '0.1'
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': ''
        ]

setup(**config)
