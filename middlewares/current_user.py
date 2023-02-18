from utils.authentication import JWTAuthentication


class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            user, type = JWTAuthentication.authenticate(request)
            if type == "customer":
                request.customer = user
                request.admin = None
            elif type == "admin":
                request.admin = user
                request.customer = None
        except:
            request.customer = None
            request.admin = None

        return self.get_response(request)
