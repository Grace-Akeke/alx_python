def raise_exception_msg(message=""):
    class CustomException(Exception):
        pass
    
    raise CustomException(message)

