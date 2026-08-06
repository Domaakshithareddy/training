from fastapi import status
from fastapi.responses import JSONResponse




class ApiResponse:


    @staticmethod
    def success(
        message: str,
        data=None,
        status_code=status.HTTP_200_OK
    ):


        return JSONResponse(
            status_code=status_code,
            content={
                "success": True,
                "message": message,
                "data": data
            }
        )


    @staticmethod
    def created(
        message: str,
        data=None
    ):


        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "success": True,
                "message": message,
                "data": data
            }
        )


    @staticmethod
    def no_content():


        return JSONResponse(
            status_code=status.HTTP_204_NO_CONTENT,
            content=None
        )


    @staticmethod
    def bad_request(
        message: str
    ):


        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "success": False,
                "message": message,
                "data": None
            }
        )


    @staticmethod
    def not_found(
        message: str
    ):


        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "success": False,
                "message": message,
                "data": None
            }
        )


    @staticmethod
    def conflict(
        message: str
    ):


        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "success": False,
                "message": message,
                "data": None
            }
        )


    @staticmethod
    def internal_server_error():


        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Internal Server Error",
                "data": None
            }
        )
