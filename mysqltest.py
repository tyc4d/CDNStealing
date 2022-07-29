import pymysql
db = pymysql.connect(host='steal.tyc4d.tw',user='user',passwd="zxc19201080",db='mydb')
cursor = db.cursor()
cursor.execute("SELECT * from visitLog")
result = cursor.fetchall()
for i in result:
    print((i[5])==b'0')
db.close()