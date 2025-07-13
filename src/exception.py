import sys
import logging

def error_message_detail(erro,detail:sys):
    _,_,exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: {file_name} at line: {line_number} with message: {str(erro)}"
    return error_message


class CustomException(Exception):
    def _init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message
    

if __name__=="__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by Zero Error")
        raise CustomException(e, sys) from e