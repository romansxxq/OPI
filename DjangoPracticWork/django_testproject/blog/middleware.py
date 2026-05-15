import time
from typing import Callable


class RequestLogMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        print(f"[{request.method}] {request.path} - {duration:.3f}s")
        response["X-App-Name"] = "MyDjangoApp"
        return response