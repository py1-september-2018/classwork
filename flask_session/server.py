from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'jkasl;kfjahwioewofkjkl'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
  session['name'] = request.form['name']
  session['favorite_language'] = request.form['favorite_language']
  session['comment'] = request.form['comment']
  return redirect('/success')

@app.route('/success')
def success():
  if 'name' not in session:
    session['name'] = "N/A"
  if 'favorite_language' not in session:
    session['favorite_language'] = "N/A"
  if 'comment' not in session:
    session['comment'] = "N/A"
  return render_template('success.html')

@app.route('/switch/<color>/<name>')
def switch(color, name):
  return render_template('switch.html', col=color, nam=name)

@app.route('/clear')
def clear():
  session.clear()
  return redirect('/')

if __name__ == "__main__":
  app.run(debug=True)