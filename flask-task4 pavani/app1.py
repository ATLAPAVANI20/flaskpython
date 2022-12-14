from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
@app.route('/')
def welcome():
    return redirect('/login')

@app.route('/home')
def home():
    return 'Login success!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'test@gmail.com' or request.form['password'] != 'test':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run( debug=True)