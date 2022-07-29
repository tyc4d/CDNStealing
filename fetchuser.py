from bs4 import BeautifulSoup
from time import sleep
from typing import Optional, Union
import pymysql as sq
import re
import requests

table_name = 'visitLog'
con = sq.connect(host='steal.tyc4d.tw',user='user',passwd="zxc19201080",db='mydb')
cur = con.cursor()

class UIDError(Exception):
    def __init__(self, uidlen : int):
        self.uidlen = uidlen
        super().__init__('The uid len is', self.uidlen)


def try_fetch(url : str) -> requests.Response:
    return requests.get(url)

def fetch_fail(e : Exception):
    print('fetch failed', e)

def try_find_uid(text : str) -> int:
    uids = re.findall(r'"uid":\d+', text)
    l = len(set(uids))
    if l != 1:
        raise UIDError(l)
    return int(uids[0].split(':')[-1])

def try_find_email(text : str) -> str:
    email = re.findall(r'"email":"[^"]+"', text)
    l = len(set(email))
    if l != 1:
        raise UIDError(l)
    return email[0].split(':')[-1]

def try_find_isAdmin(text : str) -> str:
    isAdmin = re.findall(r'"isAdmin":[^,]+', text)
    l = len(set(isAdmin))
    if l != 1:
        raise UIDError(l)
    return isAdmin[0].split(':')[-1]

def find_uid_fail(e : Exception):
    print('find uid failed', e)

def update_db(uid : int , email : str, isAdmin : str, dbid : int, cur) -> Optional[bool]:
    try:
        cur.execute(f'update {table_name} set uid = {uid}, set email = {email}, set isAdmin = {isAdmin} , visited = {True} where id = {dbid}')
        con.commit()
        return True
    except Exception as e:
        print(e)

def loop() -> int:
    # Select rows with default values
    cur.execute(f'select id, dest from {table_name} where visited!={True}')
    rows = cur.fetchall()
    print(rows)
    update_count = 0

    for row in rows:
        # print(row)
        dest = row[1] # The clicked link
        dbid = row[0]
        try:
            text = try_fetch(dest).text
            # print(text)
        except Exception as e:
            fetch_fail(e)
            continue

        try:
            uid = try_find_uid(text)
            email = try_find_email(text)
            isAdmin = try_find_isAdmin(text)
        except Exception as e:
            find_uid_fail(e)
            continue

        if update_db(uid, dbid, cur):
            update_count += 1

    return update_count

# def create_testing_db():
#     cur.execute(f'create table {table_name} (id integer primary key, clickTime text, link text, refer text, uid text, visited integer)')
#     example_items = [
#             ('1', 'hi', 'https://www.voofd.com/static/426220.css', None, 0),
#             ('1', 'hi', 'https://www.voofd.com/static/426221.css', None, 0),
#             ('1', 'hi', 'https://www.voofd.com/s/4IL16U.css', None, 0),
#             ('1', 'hi', 'https://www.voofd.com/s/1KDZ94.css', None, 0),
#             ]
#     cur.executemany(f'insert into {table_name} (clickTime, link, refer, uid, visited) values (?, ?, ?, ?, ?)', example_items)


def main():
    
    n_new_id = loop()
    print(f'Updated {n_new_id} ids')

if __name__ == '__main__':
    # create_testing_db()
    main()
