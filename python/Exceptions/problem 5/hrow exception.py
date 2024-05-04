class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
def function_that_throws_exception():
    raise MyCustomException("An error occurred in the function")
function_that_throws_exception()
