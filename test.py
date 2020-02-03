import sqlite3
from sqlite3 import Error
from flask import Flask, request
import sys
import threading

app = Flask(__name__)

@app.route("/", methods=['GET'])
def homepage():
    database = r"/suits.db"

    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute('select suit_id, checkout_time, checkin_time from suits')
    rows = cur.fetchall()
    conn.close()
    table = ""
    for row in rows:
        table += "<tr><td>"+str(row[0])+"</td><td>"+str(row[1])+"</td><td>"+str(row[2])+"</td></tr>"

    f = open("home_template.html", 'r')
    htmlstring = f.read().format(table)
    f.close()

    return htmlstring

@app.route("/action", methods=['POST'])
def actionpage():
    action = request.form['action']
    suitid = request.form['suit_id']
    return action + " " + suitid

def create_connection(db_file):
    conn=None
    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        print("THERE WAS AN ERROR")
        print(e)
    return conn

def start_server():
    app.run()

if __name__ == "__main__":
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    sys.exit()
