import sqlite3,time,shutil,os,random,string
from flask import Flask, after_this_request, render_template, request,redirect
import logging
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.CRITICAL)

app = Flask(__name__)
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/operations/',methods=["POST","GET"])
def operations():
    if request.method == "POST":
        try:
            conn = sqlite3.connect('mydb')
            c = conn.cursor()
            if request.form["iddel"] == "delete":
                c.execute(f"DELETE FROM jj")
            elif request.form["visitdel"] == "delete":
                c.execute(f"DELETE FROM visitLog")
        except Exception as e:
            print(e)
        return f'<script>alert("{e}")</script><meta http-equiv="refresh" content="0; url="../../operations">'
    else:
        return render_template('operations.html')


@app.route('/s/<path:visitPath>',methods=["GET"])
def short(visitPath):
    print(visitPath)
    newurl="https://google.com"
    try:
        nowTime = round(float(time.time()),4)
        conn = sqlite3.connect('mydb')
        refer = request.referrer
        c = conn.cursor()
        cursor = c.execute(f"SELECT createdLink from jj")
        
        for stored_link in cursor:
            print(visitPath,stored_link[0])
            if visitPath == stored_link[0]:
                cursor = c.execute(f"SELECT website from jj where createdLink='{visitPath}'")
                newurl = str(cursor.fetchone()[0]) + id_generator() +'.css'
                c.execute(f"INSERT INTO visitLog (clickTime,link,refer,dest) VALUES ('{nowTime}','{visitPath}','{refer}','{newurl}')")
                conn.commit()
                print(newurl)

            else:
                print(refer)

        conn.close()
        return redirect(newurl, code=302)
        #return f'<meta http-equiv="refresh" content="0; url="{newurl}">'
    except:
        return f'<meta http-equiv="refresh" content="0; url="https://google.com.tw">'


@app.route('/visitLogs/')
def visitLogs():
    countPayload = "";error = "";logs = []
    try:
        conn = sqlite3.connect('mydb')
        c = conn.cursor()
        cursor = c.execute("SELECT * from visitLog")
        for row in cursor:
            res = time.localtime(float(row[1]))
            timepayload = f'{res.tm_year} 年 {res.tm_mon} 月 {res.tm_mday} 日 {res.tm_hour} 時 {res.tm_min} 分 {res.tm_sec} 秒 生成'
            webpayload = f'<br /><code>隨機ID : {row[2]}</code><br />Refer : <code>{row[3]}</code><br /><a href="{row[4]}">{row[4]}</a>'
            logs.append(timepayload + webpayload)
            countPayload = f"<h1>共 {len(logs)} 筆紀錄</h1>"
            print(f'id={row[0]}')
        conn.close()
        if len(logs) == 0:
            error = f'<font size=5 color="red">目前沒有資料</font><br><p>現在時間 : {time.ctime()}</p>'
    except Exception as e:
        error = "Cannot find Sqlite DB or No DATA"
        print(e)
    return render_template('visitLogs.html', logs=logs, countPayload = countPayload, error=error)


@app.route('/entryLogs/')
def entryLogs():
    countPayload = "";error = "";logs = []
    try:
        conn = sqlite3.connect('mydb')
        c = conn.cursor()
        cursor = c.execute("SELECT * from jj")
        for row in cursor:
            res = time.localtime(float(row[1]))
            timepayload = f'{res.tm_year} 年 {res.tm_mon} 月 {res.tm_mday} 日 {res.tm_hour} 時 {res.tm_min} 分 {res.tm_sec} 秒 生成'
            
            webpayload = f'<br /><code>{row[2]}{row[3]}</code>'
            logs.append(timepayload + webpayload)
            countPayload = f"<h1>共 {len(logs)} 筆紀錄</h1>"
            print(f'id={row[0]}')
        conn.close()
        if len(logs) == 0:
            error = f'<font size=5 color="red">目前沒有資料</font><br><p>現在時間 : {time.ctime()}</p>'
    except Exception as e:
        error = "Cannot find Sqlite DB or No DATA"
        print(e)
    return render_template('entryLogs.html', logs=logs, countPayload = countPayload, error=error)

@app.route('/appendLogs/',methods=["POST","GET"])
def appendLogs():
    countPayload = "";error = "";logs = []
    if request.method == "POST":
        try:
            website = request.form["website"]
            nowTime = round(float(time.time()),4)
            print(nowTime)
            linkid = id_generator()
            conn = sqlite3.connect('mydb')
            c = conn.cursor()
            c.execute(f"INSERT INTO jj (createdTime,website,createdLink) VALUES ('{nowTime}','{website}','{linkid}')")
            conn.commit()
            conn.close()
            return '<script>alert("成功")</script><meta http-equiv="refresh" content="0; url=".">'
        except:
            return '<script>alert("Faild")</script><meta http-equiv="refresh" content="0; url=".">'
    else:
        return render_template('appendLogs.html', logs=logs, countPayload = countPayload, error=error)



@app.route('/aNa28Nss')
def give():
    url = "https://www.voofd.com/static/"
    addp = url+str(random.randint(1,100))+str(random.randint(1,100))+str(random.randint(1,100))+".css"
    nowTime = round(float(time.time()),4)
    app.logger.critical('%s visit successfully', addp)
    print(addp)
    return redirect(addp, code=302)



    
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8010, debug=True)