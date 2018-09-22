from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt

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
  
  username_query = 'SELECT username FROM users WHERE id = %(user_id)s;'
  query_data = {
    'user_id': session['user_id']
  }
  mysql = connectToMySQL('ninja_gold')
  # matching_users = mysql.query_db(username_query, query_data)
  # user = matching_users[0]

  user = mysql.query_db(username_query, query_data)[0]

  # matching_users = mysql.query_db(username_query, query_data)
  return render_template('home.html', username=user['username'])

if __name__ == '__main__':
  app.run(debug=True)