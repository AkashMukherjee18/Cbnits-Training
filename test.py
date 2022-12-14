# # a=52
# # b=100
# # print(a+b)

# "OOPS Concepts"

# from concurrent.futures import process

# class Computer:
#     ram= "16 gb"
#     processor= "i5"
#     hard_disk= "1TB"

#     def __init__(self,cpu):
#         self.cpu= cpu
#         print("This is constructor in python")
#         print("Cpu is: ",self.cpu)

#     def config(self):
#         print(self.ram,self.processor,self.hard_disk)

# com1=Computer("i 10")
# Computer.config(com1)

# # a=5
# # a.bit_length(self)

# from functools import partial


# class DoesNotExistError(Exception):
#     """Raised when a request entity is not found"""


# class NotAllowedError(Exception):
#     """Raised when an operation is not allowed"""


# class InvalidOperationError(Exception):
#     """Raised when the requested operation is invalid"""


# class InvalidArgumentError(Exception):
#     """Raised when an argument passed to a function is invalid"""


# # Error handler for Flask
# def handle_errors(code, ex):
#     return ex.args[0], code


# APP_ERROR_STATUS_CODES = {
#     DoesNotExistError: 404,
#     NotAllowedError: 403,
#     InvalidOperationError: 400,
#     InvalidArgumentError: 400,
# }

# # APP_ERROR_HANDLERS = {ex: partial(handle_errors, code) for ex, code in APP_ERROR_STATUS_CODES.items()}
# # print(APP_ERROR_STATUS_CODES)
# for ex, code in APP_ERROR_STATUS_CODES.items():
#     ex: partial(handle_errors, code)
#     print(ex,":",code)
