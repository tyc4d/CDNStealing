from distutils.sysconfig import customize_compiler
import sqlite3
conn = sqlite3.connect('mydb')
c = conn.cursor()
cursor = c.execute("SELECT * from jj")
for i in cursor:
    print(i[0],i[1],i[2],i[3])
