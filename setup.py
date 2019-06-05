import sys
from distutils.core import setup


setup_args = dict(
    name                = 'multioauthenticator',
    packages            = ['multioauthenticator'],
    version             = '0.0.1',
    description         = "MultiOAuthenticator: Authenticate JupyterHub users with multiple OAuth providers",
    author              = "Eduardo Pignatelli",
    author_email        = "epignatelli@gmail.com",
    url                 = "https://github.com/epignatelli/jupyterhub-multioauthenticator",
    license             = "GPL",
    keywords            = ['Interactive', 'Interpreter', 'Shell', 'Web'],
    entry_points={
        'jupyterhub.authenticators': [
            'multioauth = multioauthenticator.multioauthenticator:MultiOAuthenticator',
            'ldapmultioauth = multioauthenticator.multioauthenticator:LDAPMultiOAuthenticator',
        ],
    },
)

# install requirements
if 'setuptools' in sys.modules:
    setup_args['install_requires'] = install_requires = []
    with open('requirements.txt') as f:
        for line in f.readlines():
            req = line.strip()
            if not req or req.startswith(('-e', '#')):
                continue
            install_requires.append(req)


def main():
    setup(**setup_args)

if __name__ == '__main__':
    main()
