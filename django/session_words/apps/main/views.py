from django.shortcuts import render, redirect

# Create your views here.
def index(req):
  if 'word_list' not in req.session:
    req.session['word_list'] = []
  return render(req, 'main/index.html')

def add_word(req):
  if req.method != 'POST':
    return redirect('/')

  if 'size' not in req.POST:
    size = 'small'
  else:
    size = 'big'

  word = {
    'word': req.POST['word'],
    'color': req.POST['color'],
    'size': size
  }

  req.session['word_list'].append(word)
  req.session.modified = True
  print('*' * 80)
  print(req.session['word_list'])
  print('*' * 80)
  return redirect('/')

def show(req, id):
  context = {
    'user_id': id
  }
  return render(req, 'main/show.html', context)

def clear(req):
  req.session.clear()
  return redirect('/')