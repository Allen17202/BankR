from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def record(request):
    return render(request, 'transactionrecord/transaction.html')
