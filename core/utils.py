from rest_framework.response import Response

def api_response(data=None, message="", status_code=200):
    return Response({
        "success": True if status_code < 400 else False,
        "message": message,
        "data": data
    }, status=status_code)