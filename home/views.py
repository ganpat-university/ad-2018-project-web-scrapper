from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request, 'home.html',{'name':'Azhar'})

def outcome(request):
	val1=int(request.POST["city"])
	val2=int(request.POST["pagesCount"])
	res=val1+val2
	return render(request, 'result.html',{'result':res})