import sys
def error_message_detail(error,error_details):

    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=f"error occured in python script name [{file_name}] line number [{exc_tb.tb_no}] error message [{str(error)}]"
    
    return error_message

class Custom_exception(Exception):
    def __init__(self,error_message,error_details:sys):
        super.__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details=error_details)
    def __str__(self):
        return self.error_message