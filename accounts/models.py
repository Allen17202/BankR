from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class records(models.Model):
    transationID = models.IntegerField()
    senderName = models.CharField(max_length = 30)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    balance = models.IntegerField()
    def __str__(self):
        return self.senderName

class accounts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accountNumber = models.IntegerField()
    CheckingBalance = models.IntegerField()
    SavingBalance = models.IntegerField()
    recordsUser = models.ManyToManyField(records)
    def __str__(self):
        return self.user.first_name
