import datetime

from utils.jwt import generate_token


def generate_customer_token(user_id):
    payload = generate_token(
        {"user_id": user_id, "type": "customer"}, {"days": 30})
    return payload


def generate_admin_token(user_id):
    payload = generate_token(
        {"user_id": user_id, "type": "admin"}, {"days": 30})
    return payload
