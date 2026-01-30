import sys
import os
from src.logger import logging

class CustomException(Exception):
    def __init__(self,error,details:sys):
        super().__init__(error)
        self.error= error_message_formated(error,details)
        logging.info(self.error)
        

    def __str__(self):
        return self.error

    
def error_message_formated(error,details:sys):
    _,_,exc_tb=details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    
    return error_message
