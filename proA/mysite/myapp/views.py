from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home(request):
	dic1 = {
		'key': "Praveen.",
	}
	# return HttpResponse("Heloooooo World")
	return render(request, 'index.html', dic1)

def display(request):
	names=request.GET["fname"]
	return render(request, 'index.html',{"msg":"Welcome back "+names})