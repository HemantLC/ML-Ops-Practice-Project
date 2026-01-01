import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extract exact error detail information including file_name, line number and the error messege
    
    :param error: The exception that occured
    :param error_detail: The sys module to access traceback details
    :return: A formatted error messege string
    """

    # Extract traceback details (exception information)
    _,_,exc_tb = error_detail.exc_info()

    # Get the file name where the exception occured
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a formatted error messege string with the file name, line number and the actual error
    line_number = exc_tb.tb_lineno
    error_messege = f"Error occured in python script: [{file_name}] at line number [{line_number}]: {str(error)}"

    # log the error for better tracking
    logging.error(error_messege)

    return error_messege

class MyException(Exception):
    """
    Custom exception class for handling the error in the veichle ml-ops project
    """

    def __init__(self,error_messege: str,error_detail: sys):
        """
        Initilies the veichle-ml-ops exception with a detailed error messsege
        : param error_messege: A string describing the error
        : param error_detail: The sys module to access the traceback details
        """

        # Call the base class constructor with the error messege
        super.__init__(error_messege)

        # Format the detailed error messege using the def error_message_detail(error: Exception, error_detail: sys) -> str:

        self.error_messege = error_message_detail(error_messege,error_detail)


def __str__(self) -> str:
    """
    Represents the string representation of the error messege
    """
    return self.error_messege