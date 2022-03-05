from socketclient import run_socket_client
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
from threading import Thread
from sqldb import *
import json

app = Flask("NimoVIP")
app.config["DEBUG"] = False
sio = SocketIO(app)

@app.route("/")
def form():
	return render_template('jackpot.html')

@app.route("/jpval", methods=["GET"])
def get_all_jp():
	db = sqldb()
	curs = db.get_record(1000)
	records = curs.fetchall()
	data = {}
	data["data"] = records;
	return json.dumps(data)

def send_result_to_client(stype, rs):
	sio.emit(stype, rs, broadcast=True)
	#pass

@sio.on('connect')
def on_connect():
    print('Server received connection')

@sio.on('message')
def on_message(msg):
    print(msg)

@sio.on('authen')
def handle_authentication(json):
    print('received json: ' + str(json))

def run_flask():
	sio.run(app)
	# app.run(host='0.0.0.0', debug=False)

if __name__ == '__main__':
	print(send_result_to_client)
	Thread(target=run_socket_client, args=[send_result_to_client]).start()
	run_flask()