pgbackup
==============

CLI for  backing up remote PostgreSQL databases locally or to AWS S3

Preparing for developement
--------------------------------------------------------------------------

1. Endsure ``pip`` and ``pipenv`` are installed

sudo -H pip install -U pipenv
pip install --user pipenv
mkdir -p pgbackup
cd pgbackup
pipenv install --two
pipenv shell(enable virt env)

2. Clone repository: TODO provide github link

3. Create README.rst
4. Fetch developement dependencies: ``make install``



Usage
--------------------------------------------------------------------------

Pass in a full database URL, the storage driver, and destination

S3 example with bucket name:

$ pgbackup postgres://bob@examole.com:5432/db_one --driver s3 backups/dump.sql

Running Tests:
-------------------------------------------------------------------------

Run tests locally using ``make`` if virtualenv is active:

::
    $ make

If virtualenv isn't active then use:

::
    $ pipenv run make



