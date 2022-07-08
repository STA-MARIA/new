from django.shortcuts import render, redirect
from django.http import HttpResponse
from CTList.models import *

def MainPage(request):
	return render(request, 'mainpage.html')

def FirstPage(request):
	if request.method == 'POST':
		User.objects.create(name=request.POST['for1Form'],
			number=request.POST['for2Form'],
			email=request.POST['for3Form'])
		return redirect('/registration')
	brandx = User.objects.all()
	return render(request, 'page1.html', {'warehouse': brandx})

def DelUser(request, userID):
	deleteuser=User.objects.get(User_ID=userID)
	deleteuser=delete()
	return redirect('/registration')
	return render(request, 'page1.html', {'warehouse': brandx})

def SecondPage(request):
	if request.method == 'POST':
		Subscription.objects.create(namesub=request.POST['namesubs'],
			plan=request.POST['feat'])
		return redirect('/subscription')
	brandy = Subscription.objects.all()
	return render(request, 'page2.html', {'warehouse2': brandy})

def ThirdPage(request):
	if request.method == 'POST':
		Feedback.objects.create(nameuser=request.POST['nameresp'],
			game=request.POST['gameresp'],
			response=request.POST['comresp'])
		return redirect('/feedback')
	brandz = Feedback.objects.all()
	return render(request, 'page3.html', {'warehouse3': brandz})

def FourthPage(request):
	return render(request, 'page4.html')
		
def FifthPage(request):
	return render(request, 'page5.html')
