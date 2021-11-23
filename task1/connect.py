#!/usr/bin/python
import psycopg2
from config import config


def get_parts(organisation_id):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor object for execution
        cur = conn.cursor()
        
        # another way to call a function
        # cur.execute("SELECT * FROM test_sch.prashantverma_return_dep_people( %s); ",(organisation_id,))
        cur.callproc('test_sch.prashantverma_return_dep_people', (organisation_id,))

        # process the result set
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
       
	# close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            

if __name__ == '__main__':
    get_parts('5a9e003fa6da98d9852ccf13')
