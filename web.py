import sqlite3,time,shutil,os,random
from flask import Flask, render_template, request,redirect
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.CRITICAL)

app = Flask(__name__,static_folder='imgs/')

def create_id():
    now_time = int(time.time())
    print(now_time)

@app.route('/')
def root_menu():
    return 'nothing'

@app.route('/append')
def append_log():
    # conn = sqlite3.connect('mydb')
    # c = conn.cursor()
    # cursor = c.execute("INSERT INTO jj ")
    aa = 123

@app.route('/aNa28N')
def give():
    url = "https://voofd.com/"
    addp = url+str(random.randint(1,100))+str(random.randint(1,100))+str(random.randint(1,100))
    app.logger.critical('%s visit successfully', addp)
    print(addp)
    
    return redirect(addp, code=302)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8010, debug=True)
