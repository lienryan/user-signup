from flask import Flask, request, redirect, render_template

import string


app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/")

def index():

    return redirect("/signup")



@app.route("/signup")

def DisplaySignup():

    return render_template('signupForm.html')


@app.route("/signup", methods= ['POST'])

  

def validate():

    username = request.form['username']

    password = request.form['password']

    verify = request.form['verify']

    email = request.form['email']


    username_error = ""

    password_error = ""

    verify_error = ""

    email_error = ""



    #Validate username NOT: empty, contains a space character or consists of less than 3 characters 
    # or more than 20 characters 

    if  username == "":
        username_error = "You can't leave Username blank. Username must has 3 - 20 characters."
        username = ""
    elif len(username) > 20 or len(username) < 3:
        username_error = "Username must has 3 - 20 characters"
        username = ""
    
    for i in username:
      if i.isspace():
        username_error = 'Username cannot contain spaces.'
        username = ''
        
    #Validate password NOT: empty, contains a space character or consists of less than 3 characters or more than 20 characters
    #The user's password and password-confirmation must match.

    if password == "":
        password_error = "You can't leave Password blank. Password must has 3 - 20 characters."
        password=""
    elif len(password) > 20 or len(password) < 3:
        password_error = "Password must has 3 - 20 characters"
        password = ""
    if not password == verify:
        verify_error = "The passwords don't match"
        password = ""
    for i in password:
      if i.isspace():
        password_error = 'Password cannot contain spaces.'
        password = ''


    #The email field may be left empty, but if there is content in it, then it must be validated. 
    #The criteria for a valid email address in this assignment are that it has a single @, a single .,
    #contains no spaces, and is between 3 and 20 characters long.
    if len(email)>=1:
      if email != '' and (email.count("@") != 1 or email.count(".") != 1):
        email_error = "Email must has a single @, a single ., contains no spaces."
        email = ""
      elif len(email) > 20 or len (email) < 3:
        email_error = "Email must has 3 - 20 characters"
        email = ""
    for i in email:
      if i.isspace():
        email_error = 'Email cannot contain spaces.'
        email = ''



    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username= {0}'.format(username))
        #return "<h1> Hello, "+ username +"! </h1>"

    else:

        return render_template('signupForm.html', 

            username= username, username_error= username_error, 

            password_error= password_error, verify_error= verify_error,

            email= email, email_error= email_error)



@app.route('/welcome')

def welcome():

    username = request.args.get('username')

    return render_template('welcome.html', username= username)


app.run()

