#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request
from application.models.schema import *
from application.models import user_manager



@app.route('/signup')
def signup() :
	return render_template('signup.html')


@app.route('/join_submit', methods = ['POST', 'GET'])
def join_submit() :
	if request.method == 'POST':
		user_manager.add_user(request.form)
		return render_template('login.html')
	else:
		render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404