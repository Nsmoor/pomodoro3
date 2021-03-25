# Import and setup logging
import logging
log_format = "[%(levelname)s] %(asctime)s [%(module)s:%(lineno)d] %(message)s"
logging.basicConfig(format=log_format, level=logging.DEBUG)

# Import classes
from pomodoro import Pomodoro
# Import the signal module to catch CTRL+C events
import signal

# Import the package for the web server
from flask import Flask
# Import the package SocketIO for the WebSocket
from flask_socketio import SocketIO

# Create a webserver object called 'Shared Pomodoro' and keep track of it in the variable called server
server = Flask("Shared Pomodoro")
# Create a socketio object to handle web sockets


# Define an HTTP route / to serve the pomodoro page
@server.route('/')
# Define the function 'serve_index_page()' and connect it to the route /
def serve_index_page():
    # Return the static file 'index.html'
    return server.send_static_file('index.html')

socketio = SocketIO(server, cors_allowed_origins="*")

def handle_control_c(signal, frame):
  pomodoro.stop()
  exit()


#construct a pomodoro object
pomodoro = Pomodoro()
pomodoro.start()
signal.signal(signal.SIGINT, handle_control_c)
pomodoro.press()

# Start the webserver
socketio.run(server, host="0.0.0.0", debug = True)