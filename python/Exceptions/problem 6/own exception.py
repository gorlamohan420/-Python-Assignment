class CustomException(Exception):
    def __init__(self, message=""):
        self.message = message
    def __str__(self):
        return f"CustomException: {self.message}"
def function_that_raises_exception():
    raise CustomException("An error occurred in the function")
try:
    function_that_raises_exception()
except CustomException as e:
    print(e)
