from django.db import models
from ..users.models import User
# Create your models here.
class CorrespondenceManager(models.Manager):
  pass

class Correspondence(models.Model):
  created_by = models.ForeignKey(User, related_name="messages_sent")
  sent_to = models.ForeignKey(User, related_name="messages_received")
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)