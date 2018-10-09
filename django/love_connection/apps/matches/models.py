from django.db import models
from ..users.models import User

# Create your models here.
class MatchManager(models.Manager):
  pass

class Match(models.Model):
  user = models.ForeignKey(User, related_name="matched_to")
  matched_user = models.ForeignKey(User, related_name="matched_from")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)