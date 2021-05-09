from django.shortcuts import render
from django.db import models
from .models import employee

# Create your views here.
def home(request):
	return render( request, 'base.html')


def addperson(request):
	responseDic = {}
	try:
		Name = request.POST['name']
		Adderess = request.POST['address']
		emplist = employee(name=Name,address=Adderess)
		emplist.save()
		responseDic["msg1"]="Employee Added"
		return render(request, "base.html", responseDic)

	except Exception as e:
		 print(e)
		 responseDic["msg1"]="Employee cannot be Added"
		 return render(request, "base.html", responseDic)


def display(request):
	empdtls = employee.objects.all()
	empdtl = employee.objects.get(id=1)
	return render(request,"base.html",{
		'empdtls': empdtls,
		'empdtl': empdtl,
		})


def delete(request):
	nameD = request.POST['name']
	empdtls = employee.objects.filter(name=nameD)
	empdtls.delete()
	return render(request, "base.html", {"msg":nameD + " deleted"})






