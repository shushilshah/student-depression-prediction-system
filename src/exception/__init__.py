import sys
import logging


def error_message_detail(error: Exception, error_detail: sys) -> str:

    # extract traceback details
    _, _, exc_tab = error_detail.exc_info()

    # get file name where the exception occured
    file_name = exc_tab.tb_frame.f_code.co_filename

    # create a formatted error message string with file name, line number, and the actual error
    line_number = exc_tab.tb_lineno
    error_message = f"Error occured in python script: [{file_name}] at line number [{line_number}]: {str(error)}"

    # log the error for better tracking
    logging.error(error_message)

    return error_message


class MyException(Exception):
    def __init__(self, error_message: str, error_detail: sys):

        super().__init__(error_message)

        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:

        return self.error_message
