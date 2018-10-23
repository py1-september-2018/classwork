from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from ..matches.models import Match

from django.core import serializers
import json
# Create your views here.
def index(req):
  if 'user_id' not in req.session:
    return redirect('users:new')

  # user = User.objects.get(id=req.session['user_id'])
  # print(user.matched_to.all())
  # Article.objects.filter(reporter__first_name='John', reporter__last_name='Smith')

  current_user_matches_sent = Match.objects.filter(user_from=req.session['user_id'])
  current_user_matches_received = Match.objects.filter(user_to=req.session['user_id'])
  
  context = {
    'mutual_matches': User.objects.filter(matched_to__in=current_user_matches_received).filter(matched_from__in=current_user_matches_sent),
    'matches_received': User.objects.filter(matched_to__in=current_user_matches_received),
    'matches_to': User.objects.filter(matched_from__in=current_user_matches_sent),
    # 'not_matched': User.objects.exclude(matched_from=current_user_matches_sent).exclude(id=req.session['user_id'])
    'not_matched': User.objects.exclude(matched_from__in=current_user_matches_sent).exclude(id=req.session['user_id'])
  }
  return render(req, 'users/index.html', context)

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

def logout(req):
  req.session.clear()
  return redirect('users:new')

def update(req, id):
  pass

def delete(req, id):
  pass

def new(req):
  return render(req, 'users/new.html')

def edit(req, id):
  pass

def show(req, id):
  if 'user_id' not in req.session:
    return redirect("users:new")
  
  try:
    user = User.objects.get(id=id)
  except:
    return redirect("users:index")


  current_user_matches_received = user.matched_from.all()
  current_user_matches_sent = user.matched_to.all()

  context = {
    'user': user,
    'mutual_matches': User.objects.filter(matched_from__in = current_user_matches_sent).filter(matched_to__in = current_user_matches_received)
  }
  return render(req, 'users/show.html', context)

def search(req):
  users = User.objects.filter(first_name__istartswith=req.POST['searchString'])
  return HttpResponse(serializers.serialize("json", users), content_type="application/json", status=200)