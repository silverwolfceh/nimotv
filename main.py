from socketclient import run_socket_client
from flask import Flask, render_template, request
#from siosrv import send_result_to_client, run_socket_server
from threading import Thread

app = Flask("NimoVIP")
app.config["DEBUG"] = False

@app.route("/")
def form():
	return render_template('index.html')

def run_flask():
	app.run(host='0.0.0.0', debug=False)

if __name__ == '__main__':
	Thread(target=run_socket_client).start()
	#Thread(target=run_socket_server).start()
	run_flask()