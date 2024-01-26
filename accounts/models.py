from django.db import models
from django.contrib.auth.models import AbstractUser


class AuthCompany(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table = "auth_company"


class AuthUserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table = "auth_user_profile"


class AuthUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(AuthCompany, on_delete=models.DO_NOTHING, blank=False, null=True)
    profile = models.ForeignKey(AuthUserProfile, on_delete=models.DO_NOTHING, blank=False, null=True)

    class Meta:
        db_table = "auth_user"
