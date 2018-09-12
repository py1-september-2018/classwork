from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', title='home', words=['this', 'is', 'cool'])

@app.route('/process', methods=['POST'])
def process():
  return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)