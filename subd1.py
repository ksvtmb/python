# sudb test
# import sys

# sys.path.append(R"Python27\Lib\site-packages")

import pymysql

# Open database connection
db = pymysql.connect("localhost","kas","kaqt3gor","sandbox" )

sql="select name from depart order by id"

# prepare a cursor object using cursor() method
cursor = db.cursor()

cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)


# try:
   # Execute the SQL command
    # cursor.execute(sql)
   # Fetch all the rows in a list of lists.
    # results = cursor.fetchall()
    
    # for row in results:
        # print ("position",row[0]);
   
# except:
   # print ("Error: unable to fetch data")


# disconnect from server
db.close()