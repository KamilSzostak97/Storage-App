from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
	context = {}
	return render(request, 'storage/home.html', context)