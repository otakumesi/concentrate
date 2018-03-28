import concentrate
import sys
from setuptools import setup


if sys.version_info[0] < 3:
    sys.exit('python < 3 unsupported.')

    requirements = ['yaml'],

setup(
        name='concentrate',
        version=concentrate.__version__,
        packages=['concentrate'],
        license=['MIT'],
        description='',
        author=concentrate.__author__,
        author_email='bakednt@gmail.com',
        url='',
        scripts=['bin/concentrate']
        )
