import datetime
from .base import BaseManager


class AdminManager(BaseManager):
    def create_admin(self, email, username, fullname, password):
        admin = self.model(
            email=email.lower(),
            username=username.lower(),
            fullname=fullname,
        )
        admin.last_login = datetime.datetime.utcnow()
        admin.set_password(password)
        admin.save()
        return admin
