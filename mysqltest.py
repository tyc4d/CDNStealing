from distutils.sysconfig import customize_compiler
import sqlite3
conn = sqlite3.connect('mydb')
c = conn.cursor()
cursor = c.execute(f"SELECT createdLink from jj where createdLink='87JRGR'")
print(cursor.fetchone()[0])