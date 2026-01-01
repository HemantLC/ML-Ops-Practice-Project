# below code is to check the logging config

#from src.logger import logging
#logging.debug("This is a debug messege")
#logging.info("This is a info messege")
#logging.warning("This is a warning messege")
#logging.error("This is a error messege")
#logging.critical("This is a crictle error messege")

from src.logger import logging
from src.exception import MyException
import sys

try:
    a = 1 + 'x'
except Exception as e:
    logging.info(e)
    raise MyException(e,sys) from e