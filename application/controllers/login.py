#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request, session
from application.models.schema import *
from application.models import user_manager

@app.route('/login', methods = ['POST', 'GET'])
def login() :
	if request.method == 'POST':
		email = request.form['email']
		pw = request.form['password']
		result = user_manager.login_check(email,pw)
		if result:
			message = "login success!"
			session['logged_in'] = True
			login_user_data = User.query.filter(User.email == request.form['email']).first()
			session['user_id'] = login_user_data.id
			session['email'] = request.form['email']
			return render_template('contents.html', message = message)
		else:
			error = "login fail"
			return render_template('login.html', error = error)
	else:
		return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	session.pop('email', None)
	return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404