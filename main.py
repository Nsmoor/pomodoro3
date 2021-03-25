# Import 
import logging
from pomodoro import Pomodoro
import signal

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