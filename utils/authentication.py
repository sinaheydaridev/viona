from apps.models.customer import Customer
from apps.models.admin import Admin

from utils.query import get_object
from utils.jwt import verify_token


class JWTAuthentication():

    def authenticate(request):
        authorization_header = request.headers.get("Authorization", None)

        if authorization_header is None or "Bearer" not in authorization_header:
            return None

        try:
            token = authorization_header.split()[1]
            user_payload = verify_token(token)
            type = user_payload["type"]
            if type == "customer":
                user = get_object(Customer, user_payload["user_id"])
            if type == "admin":
                user = get_object(Admin, user_payload["user_id"])
        except:
            pass

        return user, type
