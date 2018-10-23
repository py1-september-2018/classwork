from django.shortcuts import render, redirect
from .models import Match

# Create your views here.
def create(req):
  Match.objects.add_match(req.POST)
  return redirect('users:index')

def delete(req):
  Match.objects.remove_match(req.POST)
  return redirect('users:index')