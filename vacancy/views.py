from django.shortcuts import render
from django.http import HttpResponse

def index(reqest):
	return HttpResponse("<h3>Hello</h3>")

# Create your views here.
