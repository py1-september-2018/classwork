from django.shortcuts import render, redirect

# Create your views here.
def index(request):
  return render(request, 'first_app/index.html')

def new_route(request):
  return render(request, 'first_app/new_route.html')