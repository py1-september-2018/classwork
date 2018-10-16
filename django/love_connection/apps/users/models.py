from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
  def validate(self, form):
    errors = []

    if len(form['first_name']) < 3:
      errors.append('First name must be at least 3 characters long')
    if len(form['last_name']) < 3:
      errors.append('Last name must be at least 3 characters long')
    if not EMAIL_REGEX.match(form['email']):
      errors.append('Email must be valid')
    if len(form['password']) < 8:
      errors.append('Password must be at least 8 characters long')
    if not 'gender' in form:
      errors.append('Must select a gender')
    if len(form['description']) < 3:
      errors.append('Description must be at least 3 characters long')
    if len(form['description']) > 255:
      errors.append('Description must not exceed 255 characters')
    if form['birth_date'] == "":
      errors.append('Must select a birth date')

    # self.filter(email=form['email'])
    try:
      self.get(email=form['email'])
      errors.append('Email already in use')
    except:
      pass
    
    return errors

  def create_user(self, user_data):
    # hash the user's password
    pw_hash = bcrypt.hashpw(user_data['password'].encode(), bcrypt.gensalt())
    # create user
    user = self.create(
      first_name=user_data['first_name'],
      last_name=user_data['last_name'],
      email=user_data['email'],
      gender=user_data['gender'],
      birth_date=user_data['birth_date'],
      pw_hash=pw_hash
    )
    return user

  def login(self, form):
    # find the user with the given email address
    user_list = self.filter(email=form['email'])
    if len(user_list) > 0:
      # email found
      user = user_list[0]
      if bcrypt.checkpw(form['password'].encode(), user.pw_hash.encode()):
        # email and password match
        return (True, user.id)
      else:
        # password does not match
        return (False, "Email or password incorrect.")
    else:
      # email not found
      return (False, "Email or password incorrect.")

class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  gender = models.CharField(max_length=255)
  pw_hash = models.CharField(max_length=500)
  description = models.CharField(max_length=255)
  birth_date = models.DateTimeField()
  matches = models.ManyToManyField("self")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()
  def __str__(self):
    name = self.email
    return name