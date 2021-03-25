# Import and setup logging
import logging
log_format = "[%(levelname)s] %(asctime)s [%(module)s:%(lineno)d] %(message)s"
logging.basicConfig(format=log_format, level=logging.DEBUG)
