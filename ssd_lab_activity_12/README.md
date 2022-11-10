# Karan Bhatt - 2022202003

## SSD Lab 13

Login and registration endpoints using Flask and flask_login.

### Class User:

-username

-email

-password

### App routes:

-/user/signup

-/user/signin

-/user/signout


register() method takes username, email and password from the form and adds it to user.db

do_signin() method takes json of request and matches email and password with the user.db and returns 200 if login successful else 500 with error message

logout() method clears session and logs out user


### To run:
python3 server.py
