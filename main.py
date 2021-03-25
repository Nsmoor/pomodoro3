# Import 
import logging
from pomodoro import Pomodoro
import signal
# Import the package for the web server
from flask import Flask
# Import the package SocketIO for the WebSocket
from flask_socketio import SocketIO

#setup logging
log_format = "[%(levelname)s] %(asctime)s [%(module)s:%(lineno)d] %(message)s"
logging.basicConfig(format=log_format, level=logging.DEBUG)

def handle_control_c(signal, frame):
  pomodoro.stop()
  exit()


#construct a pomodoro object
pomodoro = Pomodoro()
pomodoro.start()
signal.signal(signal.SIGINT, handle_control_c)
pomodoro.press()