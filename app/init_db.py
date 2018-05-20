import os
import MySQLdb

from main import create_app
from model import db
from config import DB_HOST, DB_PASS, DB_NAME, DB_USER


ROOT_DB_PASSW = os.environ.get('ROOT_DB_PASSW', False)


def main():

    if all([DB_HOST, DB_PASS, DB_NAME, DB_USER, ROOT_DB_PASSW]):

        con = MySQLdb.connect(DB_HOST, 'root', ROOT_DB_PASSW)

        cur = con.cursor()

        cur.execute('SELECT VERSION();')
        print('Mysql Version: ', cur.fetchone()[0])

        command = 'CREATE DATABASE {} CHARACTER SET utf8;'.format(DB_NAME)
        print(command)
        cur.execute(command)

        command = "CREATE USER '{}' IDENTIFIED BY '{}';".format(
            DB_USER, DB_PASS)
        print(command)
        cur.execute(command)

        command = "GRANT ALL ON {}.* TO '{}'@'%';".format(DB_NAME, DB_USER)
        print(command)
        cur.execute(command)

        cur.execute('show databases;')
        print('Mysql databases: ', *cur.fetchall(), sep='\n')

        con.close()

    db.create_all(app=create_app())


if __name__ == '__main__':
    main()
