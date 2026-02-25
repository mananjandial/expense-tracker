from rest_framework.views import exception_handler
from core.utils import error_response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return error_response(
            message="Something went wrong",
            errors=response.data,
            status_code=response.status_code
        )

    return response
