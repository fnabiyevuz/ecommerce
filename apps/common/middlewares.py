from django.utils.deprecation import MiddlewareMixin


class FingerPrintMiddleware(MiddlewareMixin):
    def process_request(self, request):
        fingerprint = request.headers.get("FINGERPRINT", None)
        setattr(request, "fingerprint", fingerprint)
