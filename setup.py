from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name='DjangoPackageTest',
    version='0.1.2',
    description='This is a Django project hashed with cython,'
                ' for testing purposes only. In the \'util.hello_world\''
                ' there is a hello world function.',
    author='Maxim Adamyan',
    author_email='maximadamyan2@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0.0',
    ],
    ext_modules=cythonize(['util/hello_world.py']),
)
