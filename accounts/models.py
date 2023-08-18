from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    MAKER = 'maker'
    CHECKER = 'checker'
    STAFF = 'staff'
    USER_ROLES = (
        (MAKER, 'Maker'),
        (CHECKER, 'Checker'),
        (STAFF, 'staff')
    )
    
    role = models.CharField(max_length=10, choices=USER_ROLES, default=STAFF)

    # Add any additional fields you might need for your users
    # For example: phone_number, address, etc.

    def is_maker(self):
        return self.role == self.MAKER

    def is_checker(self):
        return self.role == self.CHECKER