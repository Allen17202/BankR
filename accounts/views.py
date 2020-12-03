from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import accounts
from django.core.exceptions import ObjectDoesNotExist
from . import models
from .models import records
# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return render(request, 'accounts/home.html')
        else:
            return render(request, 'accounts/login.html', {'error':'Username or Password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/home.html')

def transfer(request):
    if request.method == 'POST':
        if 'checkings' in request.POST:
            try:
                receiveuser = models.accounts.objects.get(accountNumber=request.POST['accountNum'])
                #return redirect("../")#return redirect("../", {'error', 'User does not exist with this account number'})
            except ObjectDoesNotExist:
                return render(request, 'accounts/transfer.html', {'error':'User does not exist with this account number'})

            curruser = request.user
            tranferAmt = request.POST['transferNum']

            if int(tranferAmt) > curruser.accounts.CheckingBalance:
                return render(request, 'accounts/transfer.html', {'error':'Insufficient Funds'})

            curruser.accounts.CheckingBalance = curruser.accounts.CheckingBalance - int(tranferAmt)
            receiveuser.CheckingBalance = receiveuser.CheckingBalance + int(tranferAmt)
            curruser.accounts.save()
            receiveuser.save()

            item = records(transationID = receiveuser.accountNumber, senderName = receiveuser.user.first_name, amount = int(tranferAmt),balance = curruser.accounts.CheckingBalance)
            item.save()
            curruser.accounts.recordsUser.add(item)
            curruser.accounts.save()

            item2 = records(transationID = curruser.accounts.accountNumber, senderName = curruser.accounts.user.first_name, amount = int(tranferAmt),balance = receiveuser.CheckingBalance)
            item2.save()
            receiveuser.recordsUser.add(item2)
            receiveuser.save()
            return redirect("../")
        elif 'savings' in request.POST:
            try:
                receiveuser = models.accounts.objects.get(accountNumber=request.POST['accountNum'])
            except ObjectDoesNotExist:
                return render(request, 'accounts/transfer.html', {'error':'User does not exist with this account number'})

            curruser = request.user
            tranferAmt = request.POST['transferNum']

            if int(tranferAmt) > curruser.accounts.SavingBalance:
                return render(request, 'accounts/transfer.html', {'error':'Insufficient Funds'})

            curruser.accounts.SavingBalance = curruser.accounts.SavingBalance - int(tranferAmt)
            receiveuser.SavingBalance = receiveuser.SavingBalance + int(tranferAmt)
            curruser.accounts.save()
            receiveuser.save()

            item = records(transationID = receiveuser.accountNumber, senderName = receiveuser.user.first_name, amount = int(tranferAmt),balance = curruser.accounts.SavingBalance)
            item.save()
            curruser.accounts.recordsUser.add(item)
            curruser.accounts.save()

            item2 = records(transationID = curruser.accounts.accountNumber, senderName = curruser.accounts.user.first_name, amount = int(tranferAmt),balance = receiveuser.SavingBalance)
            item2.save()
            receiveuser.recordsUser.add(item2)
            receiveuser.save()

            return redirect("../")
    return render(request, 'accounts/transfer.html')
def record(request):
    record = request.user.accounts.recordsUser.all()
    return render(request, 'accounts/transaction.html', {'records':record})
