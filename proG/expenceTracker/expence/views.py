import expence
from django import db
from django.shortcuts import render
from django.db import models
from .models import expences, inibal            
# Create your views here.

def home(request):
    return render(request, 'home.html')

def inibalance(request):
    responseDict = {}
    chkini = inibal.objects.filter(id=1).exists()
    if chkini == False:
        inBalance = request.POST['inibal']
        dbIn = inibal(inibalance = inBalance )
        dbIn.save()
        responseDict['msg'] = 'initial balence set to ', inBalance
    else:
        inBalance = inibal.objects.get(id = 1)
        responseDict['msg'] = 'initial balence set to ' + str(inBalance.inibalance)
    return render(request, 'home.html', responseDict)

def addExpence(request):
    responseDict = {}
    expName = request.POST['expname']
    expAmt = int(request.POST['expamt'])
    val = inibal.objects.get(id = 1)
    amt = val.inibalance
    if (amt>expAmt):
        chkExpName  = expences.objects.filter(expence = expName).exists()
        if chkExpName == True:
            expence = expences.objects.get(expence = expName)
            oVal = expence.price
            nVal = oVal + expAmt
            expence.price = nVal
            expence.save()
            inBalance = amt - expAmt
            val.inibalance = inBalance
            val.save()
            responseDict['msg1'] = 'expence Updated'
        else:
            dbIn = expences(expence = expName, price = expAmt)
            dbIn.save()
            amt = val.inibalance
            inBalance = amt - expAmt
            val.inibalance = inBalance
            val.save()
            responseDict['msg1'] = 'expence Added'
        return render(request, 'home.html', responseDict)
    else:
        responseDict['msg1'] = 'Amount exceeded'
        return render(request, 'home.html', responseDict)

def display(request):
    expList = expences.objects.all()
    inibals = inibal.objects.get(id = 1)
    return render(request, 'home.html', {
        'expence': expList,
        'bal': inibals,
    })