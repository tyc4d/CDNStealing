import sqlite3,time,shutil,os,random,requests
from flask import Flask, render_template, request,redirect
import logging
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.CRITICAL)

app = Flask(__name__,static_folder='imgs/')

def create_id():
    now_time = int(time.time())
    print(now_time)

@app.route('/')
def root_menu():
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

@app.route('/aNa28Nss')
def give():
    url = "https://www.voofd.com/static/"
    addp = url+str(random.randint(1,100))+str(random.randint(1,100))+str(random.randint(1,100))+".css"
    app.logger.critical('%s visit successfully', addp)
    print(addp)
    return redirect(addp, code=302)
    
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8010, debug=True)
