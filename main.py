from socketclient import run_socket_client
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
from threading import Thread
from sqldb import *
from util import create_stats_data
import json
from datetime import date

app = Flask("NimoVIP")
app.config["DEBUG"] = False
sio = SocketIO(app)

@app.route("/")
def form():
	return render_template('beanlot.html')

@app.route("/jp")
def beanlotform():
	return render_template('jackpot.html')

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
	curs = db.get_record(2900)
	records = curs.fetchall()
	data = {}
	data["data"] = records;
	return json.dumps(data)

@app.route("/beanboxfilter", methods=["GET"])
def get_all_beanbox_filter():
	boxid = request.args.get("boxid")
	db = beanlotdb()
	curs = db.get_record_filter(int(boxid), 2900)
	records = curs.fetchall()
	data = {}
	data["data"] = records;
	return json.dumps(data)

@app.route("/beanlottoday", methods=["GET"])
def get_all_beanbox_today():
	db = beanlotdb()
	curs = db.get_record_today(2900)
	records = curs.fetchall()
	data = {}
	data["data"] = records;
	return json.dumps(data)

@app.route("/beanlotstats", methods=["GET"])
def get_bean_box_stats():
	filtermode = request.args.get("filter")
	if filtermode == "day":
		db = beanlotdb()
		dd = request.args.get("dd")
		mm = request.args.get("mm")
		d0 = date(2022, int(mm), int(dd))
		curs = db.get_record_from_date(str(d0))
		records = curs.fetchall()
		return create_stats_data(records)
	elif filtermode == "all":
		db = beanlotdb()
		curs = db.get_record(9999)
		records = curs.fetchall()
		return create_stats_data(records)
	elif filtermode == "today":
		db = beanlotdb()
		d0 = date.today()
		curs = db.get_record_from_date(str(d0))
		records = curs.fetchall()
		return create_stats_data(records)
	else:
		pass
		
def send_result_to_client(stype, rs):
	sio.emit(stype, rs, broadcast=True)

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
	Thread(target=run_socket_client, args=[send_result_to_client, socketclient_close_cb, send_result_to_client]).start()

if __name__ == '__main__':
	Thread(target=run_socket_client, args=[send_result_to_client, socketclient_close_cb, send_result_to_client]).start()
	run_flask()