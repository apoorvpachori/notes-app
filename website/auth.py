from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods = ['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html', text="Testing")

@auth.route('/logout',methods = ['GET','POST'])
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods = ['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be longer than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('First must be longer than 1 character', category='error')
        elif password1 != password2:
            print(password1)
            print(password2)
            flash('Passwords dont match', category='error')
        else:
            flash('Account created!', category='success')
            
    return render_template('sign_up.html')