from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'post'])
def login():
    return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'post'])
def sign_up():
   if request.method == 'POST':
       email = request.form.get('email')
       firstName = request.form.get('email')
       Password1 =  request.form.get('firstName')
       password2 =  request.form.get('password2')

       if len(email) < 4:
           flash('Email must be Greater than 4 Characters.', category= 'error')
       elif len(firstName) < 2:
           flash('First name must be greater than 1 Characters.', category= 'error')
       elif Password1 != password2:
           flash('Hey!, Password Don\'t Much, Please try Again.', category= 'error')
       elif len(Password1) < 7:
           flash('Password must be at least 7 characters.', category= 'error')
       else:
           flash('Account Created!', category= 'success')

   return render_template("sign_up.html")
