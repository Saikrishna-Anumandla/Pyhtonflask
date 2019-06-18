"""Cloud Foundry test"""
from typing import Any, Union

from flask import Flask, render_template, request, send_from_directory
import sqlite3
import os
import random
import time
import array as arr
import io

app = Flask(__name__)

# print(os.getenv("PORT"))
port = int(os.getenv('VCAP_APP_PORT', '8080'))


@app.route('/')
def home():
    conn = sqlite3.connect('myDB.db')
    print("Opened database successfully")
    cur = conn.cursor()
    strt = int(round(time.time()*1000))
    print(strt)
    for x in range(0,1000):
        cur.execute("SELECT COUNT(*) from quakes WHERE mag = ?", (random.randint(0,8),))
        rows = cur.fetchone()
    else:
        end = int(round(time.time()*1000))
        print(end)
        total = end - strt
        print(total)
        return render_template('testhtml.html',rows=total)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
