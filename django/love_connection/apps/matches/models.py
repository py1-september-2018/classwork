from django.db import models
from ..users.models import User

# Create your models here.
class MatchManager(models.Manager):
  def add_match(self, form):
    error = False

    try:
      user_from = User.objects.get(id=form['user'])
    except:
      print("Cannot get user_from")
      error = True
    
    try:
      user_to = User.objects.get(id=form['matched_user'])
    except:
      print("Cannot get user_to")
      error = True

    if not error:
      self.create(user_from=user_from, user_to=user_to)
      return True
    else:
      return False
  
  def remove_match(self, form):
    # match = self.filter(user_from = form['user']).filter(user_to = form['unmatched_user'])
    # match = self.filter(user_from = form['user'], user_to = form['unmatched_user'])
    try:
      match = self.get(user_from = form['user'], user_to = form['unmatched_user'])
      match.delete()
      return True
    except:
      return False

class Match(models.Model):
  user_from = models.ForeignKey(User, related_name="matched_to")
  user_to = models.ForeignKey(User, related_name="matched_from")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = MatchManager()