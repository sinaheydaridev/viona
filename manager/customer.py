import datetime

from django.db import models


class CustomerManager(models.Manager):
    def create_customer(self, email, username, fullname, password):
        customer = self.model(
            email=email.lower(),
            username=username.lower(),
            fullname=fullname,
        )
        customer.last_login = datetime.datetime.utcnow()
        customer.set_password(password)
        customer.save()
        return customer
