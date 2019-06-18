"""Cloud Foundry test"""
from typing import Any, Union

from flask import Flask, render_template, request, send_from_directory
import sqlite3
import os
import random
import time
import io

app = Flask(__name__)

# print(os.getenv("PORT"))
port = int(os.getenv('VCAP_APP_PORT', '8080'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/pictures', methods=['POST'])
def pictures():
    if request.method == 'POST':
        num1 = request.form['num1']
        #num2 = request.form['num2']
        #text = request.form['text']
        conn = sqlite3.connect('myDB.db')
        print("Opened database successfully")
        cur = conn.cursor()
        strt = int(round(time.time() * 1000))
        print(strt)
        num1 = int(num1)
        for x in range(0, num1):
            cur.execute("SELECT COUNT(*) from quakes WHERE mag = ?", (random.randint(0,8),))
            rows = cur.fetchall()
        else:
            end = int(round(time.time() * 1000))
            print(end)
            total = (end - strt)/num1
            print(total)

            return render_template("pictures.html", rows=total)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
