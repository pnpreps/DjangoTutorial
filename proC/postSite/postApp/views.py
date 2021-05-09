from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'index.html')

def display(request):
	name = request.POST['name']
	age = int(request.POST['age'])
	if age >= 18:
		result = "Eligible to Vote."
	else:
		result = "Not Eligible to Vote."
	return render(request, 'result.html',{
		"msg": name + ' is '+ result
		})