import jwt
import datetime

from core import settings


def generate_token(payload, expire):
    payload = {
        **payload,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(**expire),
        'iat': datetime.datetime.utcnow(),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def verify_token(token):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise ValueError("Invalid token.")
    return payload
