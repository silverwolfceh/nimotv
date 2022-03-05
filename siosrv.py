from flask_socketio import SocketIO, send
sio = socketio.AsyncServer()



@sio.event
def connect(sid, environ, auth):
    print('Client connected ', sid)

@sio.event
def disconnect(sid):
    print('Client disconnected ', sid)

@sio.on('getsmalljp')
def get_smalljp(sid, data):
    pass

@sio.on('getbigjp')
def get_bigjp(sid, data):
    pass

@sio.on('gettoken')
def get_token(sid, data):
    pass

def send_result_to_client(data):
	sio.emit("result", data)

def run_socket_server(app):
     sio.run(app)
	 #web.run_app(app)

if __name__ == '__main__':
	run_socket_server()