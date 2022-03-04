import socketio
sio = socketio.Server()

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
	