from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'index.html')

def add(request):
	numa = int(request.GET['numa'])
	numb = int(request.GET['numb'])
	result = str(numa+numb)
	return render(request, 'index.html',{
		"msg": 'sum is '+ result
		})