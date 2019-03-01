from setuptools import setup, find packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backup locally or to AWS S3'
    long_description=readme,
    author='Andrzej Jakubiak'
    author_email='jakubiak@fastmail.com'
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)
