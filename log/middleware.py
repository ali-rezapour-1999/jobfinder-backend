import traceback

from .models import ErrorLog


class ErrorLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        ErrorLog.objects.create(
            user=request.user if request.user.is_authenticated else None,
            error_message=str(exception),
            stack_trace=traceback.format_exc(),
            request_data=request.POST.dict(),
        )
