#!/usr/bin/python
import psycopg2
import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config.config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn

def create_cursor(conn):
    try:
        cr = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return cr

def close_connect(conn, cr):
    try:
        if cr is not None:
            cr.close()
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
