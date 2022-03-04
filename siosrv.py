import socketio
from aiohttp import web
sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)
app.router.add_get('/', index)

async def index(request):
    """Serve the client-side application."""
    with open('templaces/index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

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

def run_socket_server():
	 web.run_app(app)

if __name__ == '__main__':
	run_socket_server()