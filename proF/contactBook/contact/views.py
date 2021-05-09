from django.shortcuts import render
from django.db import models
from .models import contactBooks

# Create your views here.
def home(request):
	return render(request, 'home.html')

def addperson(request):
	responseDic = {}
	try:
		Name = request.POST['name']
		Phone = request.POST['phone']

		chk = contactBooks.objects.filter(name=Name).exists()
		if chk == True:
			responseDic["msg0"]="Name exists"
			return render(request, "home.html", responseDic)
		else:
			contact = contactBooks(name=Name,phone=Phone)
			contact.save()
			responseDic["msg0"]="Contact Added"
			return render(request, "home.html", responseDic)

	except Exception as e:
		 print(e)
		 responseDic["msg0"]="Contact cannot be Added"
		 return render(request, "home.html", responseDic)

def display(request):
	# cnts = contactBooks.objects.get(id=6)
	cnts = contactBooks.objects.all()
	return render(request,"home.html",{
		'cnts': cnts,
		})


def delete(request):
	responseDic = {}
	Name = request.POST['name']
	chk = contactBooks.objects.filter(name=Name).exists()
	if chk == True:
		empdtls = contactBooks.objects.filter(name=Name)
		empdtls.delete()
		responseDic["msg"]="Contact deleted"
	else:
		responseDic["msg"]="Contact Not Found"
	return render(request, "home.html", responseDic)


def update(request):
	responseDic = {}
	try:
		oName = request.POST['sname']
		oNumber = request.POST['snumber']
		nName =  request.POST['Nname']
		nNumber =  request.POST['Nnumber']
		btn = name = request.POST['btn']
		if btn == 'uname':
			chkNewName = contactBooks.objects.filter(name=nName).exists()
			if chkNewName == False:
				ulist = contactBooks.objects.get(name = oName)
				ulist.name = nName
				ulist.save()
				responseDic["msg3"] = "Name Updated"
			else:
				responseDic["msg3"] = "Name exists"
			return render(request, 'home.html',responseDic)


		elif btn == 'uphone':
		    chkNewNum = contactBooks.objects.filter(phone=nNumber).exists()
		    if chkNewNum == False:
		    	ulist = contactBooks.objects.get(phone = oNumber)
		    	ulist.phone = nNumber
		    	ulist.save()
		    	responseDic["msg3"] = "Number Updated"
		    else:
		    	responseDic["msg3"] = "Number exists"
		    return render(request, 'home.html',responseDic)


	except Exception as e:
			 print(e)
			 responseDic["msg3"] = "Name or Number Dosent exists"
			 return render(request, "home.html",responseDic)

