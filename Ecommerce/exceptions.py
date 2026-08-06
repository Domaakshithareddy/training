from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

class ProductNotFoundException(Exception):
    def __init__(self,message='Product not found'):
        self.message=message

class ProductAlreadyExistsException(Exception):
    def __init__(self,message='Product already exists'):
        self.message=message

def product_not_found_exception_handler(
        request:Request,
        exception:ProductNotFoundException
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            'success':False,
            'message':exception.message,
            'data':None
        }
    )

def product_already_exists_exception_handler(
        request:Request,
        exception:ProductAlreadyExistsException
):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            'success':False,
            'message':exception.message,
            'data':None
        }
    )

def generic_exception_handler(
        request:Request,
        exception:Exception
):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            'success':False,
            'messgae':'Internal server error',
            'data':None
        }
    )

def register_exception_handlers(app:FastAPI):
    app.add_exception_handler(
        ProductNotFoundException,
        product_not_found_exception_handler
    )

    app.add_exception_handler(
        ProductAlreadyExistsException,
        product_already_exists_exception_handler
    )

    app.add_exception_handler(
        Exception,
        generic_exception_handler
    )