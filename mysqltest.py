import pymysql
db = pymysql.connect(host='steal.tyc4d.tw',user='user',passwd="zxc19201080",db='mydb')
cursor = db.cursor()
cursor.execute(f"SELECT createdLink from jj")
r = cursor.fetchone()[0]
print(r)