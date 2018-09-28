from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import connectToMySQL
from queries import *
from flask_bcrypt import Bcrypt
import random

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'asdklewioplop[jkl;'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
  errors = []
  
  if len(request.form['username']) < 3:
    errors.append('Username must be at least 3 characters long')
  if len(request.form['password']) < 8:
    errors.append('Password must be at least 8 characters long')
  if request.form['password'] != request.form['confirm']:
    errors.append("Passwords must match")

  mysql = connectToMySQL('ninja_gold')
  user_query = 'SELECT * FROM users WHERE username = %(username)s;'
  data = {
    'username': request.form['username']
  }
  users = mysql.query_db(user_query, data)

  if len(users) > 0:
    errors.append('Username already in use')
  
  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/')
  else:
    # Hash user's password for security
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    # Create user
    mysql = connectToMySQL('ninja_gold')
    insert_query = 'INSERT INTO users (username, pw_hash, gold, created_at, updated_at) VALUES (%(username)s, %(pw_hash)s, 0, NOW(), NOW());'
    insert_data = {
      'username': request.form['username'],
      'pw_hash': hashed_pw
    }
    user_id = mysql.query_db(insert_query, insert_data)
    session['user_id'] = user_id
  return redirect('/home')

@app.route('/login', methods=['POST'])
def login():
  username_query = 'SELECT * FROM users WHERE username=%(username)s'
  query_data = {
    'username': request.form['username']
  }
  mysql = connectToMySQL('ninja_gold')
  matching_users = mysql.query_db(username_query, query_data)

  if len(matching_users) == 0:
    flash('Username or password incorrect')
    return redirect('/')
  else:
    user = matching_users[0]
    if bcrypt.check_password_hash(user['pw_hash'], request.form['password']):
      session['user_id'] = user['id']
      return redirect('/home')
    else:
      flash('Username or password incorrect')
      return redirect('/')

@app.route('/home')
def home():
  if 'user_id' not in session:
    return redirect('/')
  
  username_query = 'SELECT username, gold FROM users WHERE id = %(user_id)s;'
  query_data = {
    'user_id': session['user_id']
  }
  mysql = connectToMySQL('ninja_gold')
  # matching_users = mysql.query_db(username_query, query_data)
  # user = matching_users[0]

  user_from_db = mysql.query_db(username_query, query_data)[0]

  # matching_users = mysql.query_db(username_query, query_data)

  mysql = connectToMySQL('ninja_gold')
  locations_list = mysql.query_db('SELECT * FROM locations;')

  activities_list = get_activities(session['user_id'])

  return render_template('home.html', user=user_from_db, locations=locations_list, activities=activities_list)

@app.route('/locations/new')
def new_location():
  return render_template('new_location.html')

@app.route('/locations/create', methods=['POST'])
def create_location():
  errors = []

  if len(request.form['name']) < 3:
    errors.append('Name must be at least 3 characters long.')

  try:
    min_gold = int(request.form['min_gold'])
  except ValueError:
    errors.append('Min Gold must be an integer.')

  try:
    max_gold = int(request.form['max_gold'])
  except ValueError:
    errors.append("Max Gold must be an integer")

  if 'user_id' not in session:
    errors.append('You must login to create a location.')
  
  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/locations/new')
  else:
    location_query = 'INSERT INTO locations (name, min_gold, max_gold, location_creator, created_at, updated_at) VALUES(%(name)s, %(min_gold)s, %(max_gold)s, %(user_id)s, NOW(), NOW());'
    location_data = {
      'name': request.form['name'],
      'min_gold': min_gold,
      'max_gold': max_gold,
      'user_id': session['user_id']
    }
    mysql = connectToMySQL('ninja_gold')
    mysql.query_db(location_query, location_data)
  return redirect('/home')

@app.route('/activities/<location_id>/create', methods=['POST'])
def process(location_id):
  try:
    location_id = int(location_id)
  except ValueError:
    return redirect('/home')

  location_query = 'SELECT * FROM locations WHERE id = %(location)s;'
  location_data = {
    'location': location_id
  }
  mysql = connectToMySQL('ninja_gold')
  location_list = mysql.query_db(location_query, location_data)

  try:
    location = location_list[0]
  except IndexError:
    return redirect('/home')

  gold = random.randint(location['min_gold'], location['max_gold'])

  activity_query = 'INSERT INTO activities (gold_amount, user_id, locations_id, created_at, updated_at) VALUES (%(gold)s, %(user_id)s, %(location_id)s, NOW(), NOW());'
  activity_data = {
    'gold': gold,
    'user_id': session['user_id'],
    'location_id': location['id']
  }
  mysql = connectToMySQL('ninja_gold')
  mysql.query_db(activity_query, activity_data)

  user_get = 'SELECT gold FROM users WHERE id = %(user_id)s;'
  user_data = {
    'user_id': session['user_id']
  }
  mysql = connectToMySQL('ninja_gold')
  users_list = mysql.query_db(user_get, user_data)
  user = users_list[0]

  user_query = 'UPDATE users SET gold = %(gold)s WHERE id = %(user_id)s;'
  user_data = {
    'gold': user['gold'] + gold,#old gold plus new gold,
    'user_id': session['user_id']
  }
  mysql = connectToMySQL('ninja_gold')
  mysql.query_db(user_query, user_data)

  return redirect('/home')

if __name__ == '__main__':
  app.run(debug=True)