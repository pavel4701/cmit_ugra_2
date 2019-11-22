from django.shortcuts import render

def index(reqest):
	return render(reqest, 'main_app/home_page.html')

# Create your views here.
