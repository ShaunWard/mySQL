import os
import datetime
import pymysql

#Get username

username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                                user=username,
                                password='',
                                db='Chinook')

try:
    #Run query
    with connection.cursor() as cursor:
        rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['Bob', 'Jim'])
        connection.commit()
        #Note that the above will still display a warning (not error) if the
        #table already exists
        for row in cursor:
            print(row)
finally:
    #Close the connection, regardless of whether above was successful or not
    connection.close()