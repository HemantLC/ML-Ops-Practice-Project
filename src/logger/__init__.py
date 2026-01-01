import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime


# constants for log configurations

LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_MB = 5 *1024*1024
BACK_UP_COUNT = 3 # nUMBER OF BACKUP FILES TO KEEP

#CONSTRUCT LOG FILE PATH
log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path,exist_ok=True)
log_file_path = os.path.join(log_dir_path,LOG_FILE)

def configure_logger():
    """
    Configures logging with a rotating file handler and a console handler
    """

    #Create a custom handler
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Define formatter
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    #File handler with rotation
    file_handler = RotatingFileHandler(log_file_path,maxBytes=MAX_LOG_MB,backupCount=BACK_UP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    #Console Handler

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    # Add handler to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Configure the logger
configure_logger()