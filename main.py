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

@app.route("/beanlot")
def beanlotform():
	return render_template('beanlot.html')

@app.route("/jpval", methods=["GET"])
def get_all_jp():
	db = jpdb()
	curs = db.get_record(1000)
	records = curs.fetchall()
	data = {}
	data["data"] = records;
	return json.dumps(data)

@app.route("/beanlotall", methods=["GET"])
def get_all_beanlot():
	db = beanlotdb()
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
	sio.run(app, host = '0.0.0.0', port=8888)
	# app.run(host='0.0.0.0', debug=False)

def socketclient_close_cb():
	Thread(target=run_socket_client, args=[send_result_to_client, socketclient_close_cb]).start()

if __name__ == '__main__':
	Thread(target=run_socket_client, args=[send_result_to_client, socketclient_close_cb, send_result_to_client]).start()
	run_flask()