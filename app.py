from flask import Flask, redirect, url_for, render_template
import requests
import db_connect
import json
import time
import threading
import tasks
from function.handle import getAPIHistory

app = Flask(__name__)

@app.before_first_request
def light_thread():
    def run():
        tasks.sleepUpdateCoins()
    thread = threading.Thread(target=run)
    thread.start()

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/api/crypto', methods=['POST', 'GET'])
def api_crypto():
    return {
        "listCrypto": db_connect.query()
    }

@app.route('/api/history', methods=['POST', 'GET'])
def api_history():
    list = []
    for nameCrypto in db_connect.queryName():
        list.append(getAPIHistory(nameCrypto))
    return list

if __name__ == '__main__':
    app.run(debug=True)