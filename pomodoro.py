# Import logging
import logging
from threading import Timer

#states
IDLE = 0
WORK = 1
BREAK_ALARM = 2
SHORT_BREAK = 3
WORK_ALARM = 4
LONG_BREAK = 5

class Pomodoro:
  
  def __init__(self):
    logging.debug("Construct pomodoro object")
    self.setup()

  def setup(self):
    logging.debug("Setup")
    self.currentState = IDLE
  
  def checkState(self):
    logging.debug("Check state")
    # Create an object Timer which wait 1 second before calling the method checkState and keep track of it in the attribute _nextCheck
    self._nextCheck = Timer(1, self.checkState)
    # Start the timer
    self._nextCheck.start()
    if self.currentState == IDLE:
        if self.isPressed():
            self.startWork()
    elif self.currentState == WORK:
        if self.isTimeOver():
            self.ringBreakAlarm()
    elif self.currentState == BREAK_ALARM:
        if self.isPressed():
          if self.isTimeForLongBreak():
            self.startLongBreak()
          else:
            self.startShortBreak()
    elif self.currentState == SHORT_BREAK:
        if self.isTimeOver():
            self.ringWorkAlarm()
    elif self.currentState == WORK_ALARM:
        if self.isPressed():
            self.startWork()
    elif self.currentState == LONG_BREAK:
        if self.isPressed():
            self.pause()
    else:
        # Log a warning with the state
        logging.warn("Invalid state: " + self.currentState)
      
  			
  def start(self):
    logging.debug("start Pomodoro")
    self.checkState()
  
  def stop(self):
    logging.debug("Stop Pomodoro")
    # If a timer has been constructed and waiting for the next second
    if self._nextCheck is not None:
      # Cancel the timer
      self._nextCheck.cancel()

  def changeState(self, state):
    """
    for changing states 
    state =  the new state
    """
    logging.debug("NEW STATE")
    self.currentState = state
    

  def startWork(self):
    logging.debug("Start work")

  def ringBreakAlarm(self):
    logging.debug("Ring break alarm")

  def startShortBreak(self):
    logging.debug("Start short break")

  def ringWorkAlarm(self):
    logging.debug("Ring work alarm")

  def startLongBreak(self):
    logging.debug("Start long break")

  def pause(self):
    logging.debug("Pause")

  def isPressed(self):
    logging.debug("Is Pressed?")

  def isTimeOver(self):
    logging.debug("Is time over?")

  def isTimeForLongBreak(self):
    logging.debug("Is time for long break?")

  
    
    