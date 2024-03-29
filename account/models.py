import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.CharField(max_length=64, unique=True)
    username = models.CharField(max_length=32, unique=True)
    user_profile_pic = models.CharField(max_length=256, null=True, db_column="profile_pic")
    user_language = models.CharField(max_length=10, null=True, default=None)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_name}-{self.user_id}"

    class Meta:
        db_table = "account"