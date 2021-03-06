from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8c6309c14072baaa9dfcf848f8ac5d99'

posts = [
    {
        'author': 'Tom Castagnino',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
def homepage():
  return render_template('homepage.html')

@app.route('/port/blog')
def home():
  return render_template('home.html', posts=posts)

@app.route('/port/blog/about')
def about():
  return render_template('about.html', title='About')

@app.route('/port/blog/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)

@app.route('/port/blog/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if True:
      flash(f'You have been logged in!', 'success')
      return redirect(url_for('home'))
    else:
      flash('Loggin Unsuccessful. Please check username and password', 'danger')
  return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
  app.run(debug=True)
