from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(req):
  return render(req, 'users/index.html')

def create(req):
  if req.method != 'POST':
    return redirect('users:new')

  errors = User.objects.validate(req.POST)
  if len(errors) > 0:
    for error in errors:
      messages.error(req, error)
  else:
    user = User.objects.create_user(req.POST)
    print(user)
    req.session['user_id'] = user.id
  return redirect('users:new')

def login(req):
  if req.method != 'POST':
    return redirect('users:new')

  valid, response = User.objects.login(req.POST)
  if valid == True:
    req.session['user_id'] = response
    return redirect("users:index")
  else:
    messages.error(req, response)

  return redirect("users:new")

def update(req, id):
  pass

def delete(req, id):
  pass

def new(req):
  return render(req, 'users/new.html')

def edit(req, id):
  pass

def show(req, id):
  pass