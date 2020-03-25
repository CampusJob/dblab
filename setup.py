
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dblab',
    version='0.0.1',

    description="DatabaseLab API wrapper",

    url='https://github.com/olivierpilotte/dblab',
    author='Olivier Pilotte',
    author_email='olivierpilotte@gmail.com',
    license='Apache Licence v2.0',

    packages=setuptools.find_packages(exclude=['docs', 'tests*']),

    install_requires=['requests', 'munch', 'psycopg2'],
)
