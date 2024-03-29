import re
from setuptools import setup

#
# this approach used below to determine ```version``` was inspired by
# https://github.com/kennethreitz/requests/blob/master/setup.py#L31
#
# why the complexity? wanted a single spot for the version number
#
# the code below assumes the distribution is being built with the
# current directory being the directory in which setup.py is stored
# which should be totally fine 99.9% of the time. not going to add
# the coode complexity to deal with other scenarios
#
reg_ex_pattern = r'__version__\s*=\s*[\'"](?P<version>[^\'"]*)[\'"]'
reg_ex = re.compile(reg_ex_pattern)
version = ''
with open('dev_env_testing/__init__.py', 'r') as fd:
    for line in fd:
        match = reg_ex.match(line)
        if match:
            version = match.group('version')
            break
if not version:
    raise Exception('Can''t locate project''s version number')


def _long_description():
    try:
        with open('README.rst', 'r') as f:
            return f.read()
    except IOError:
        # simple fix for avoid failure on "source cfg4dev"
        return "a long description"


_author = 'Dave Simons'
_author_email = 'simonsdave@gmail.com'


setup(
    name='dev_env_testing',
    packages=[
        'dev_env_testing',
    ],
    scripts=[
        'bin/no-op.sh',
    ],
    install_requires=[
    ],
    include_package_data=True,
    version=version,
    description='Dev Env Testing',
    long_description=_long_description(),
    author=_author,
    author_email=_author_email,
    maintainer=_author,
    maintainer_email=_author_email,
    license='MIT',
    url='https://github.com/simonsdave/dev-env-testing',
    download_url='https://github.com/simonsdave/dev-env-testing/tarball/v%s' % version,
    keywords=[
        'development',
        'tools',
        'testing',
    ],
    # list of valid classifiers @ https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
