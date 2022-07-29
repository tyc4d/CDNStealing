import sqlite3,time,shutil,os,random,string
from flask import Flask, render_template, request,redirect
import logging
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.CRITICAL)

app = Flask(__name__)
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))+'.css'

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/operations/',methods=["POST","GET"])
def operations():
    if request.method == "POST":
        try:
            shutil.rmtree("imgs")
            os.remove("mydb")
        except OSError as e:
            message = e
        else:
            message = "成功刪除"
        print(message)
        return f'<script>alert("{message}")</script><meta http-equiv="refresh" content="0; url="../../operations">'
    if request.method == "GET":
        return render_template('operations.html')
    else:
        return "Error"

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
            webpayload = f'<br /><code>{row[2]}</code>'
            linkid=f'<br /><code>{row[3]}</code>'
            logs.append(timepayload + webpayload + linkid)
            countPayload = f"<h1>共 {len(logs)} 筆紀錄</h1>"
            print(f'id={row[0]}')
        conn.close()
        if len(logs) == 0:
            error = f'<font size=5 color="red">目前沒有資料</font><br><p>現在時間 : {time.ctime()}</p>'
    except:
        error = "Cannot find Sqlite DB or No DATA"
        print(error)
    return render_template('entryLogs.html', logs=logs, countPayload = countPayload, error=error)

@app.route('/appendLogs/',methods=["POST","GET"])
def appendLogs():
    countPayload = "";error = "";logs = []
    if request.method == "POST":
        website = request.form["website"]
        nowTime = round(float(time.time()),4)
        linkid = id_generator()
        conn = sqlite3.connect('mydb')
        c = conn.cursor()
        c.execute(f"INSERT INTO jj (createdTime,website,createdLink) VALUES ({website},{nowTime},{linkid})")
        conn.commit()
        conn.close()
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
