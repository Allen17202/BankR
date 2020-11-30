from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class AccountInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accountNumber = models.IntegerField()
    CheckingBalance = models.IntegerField()
    SavingBalance = models.IntegerField()
