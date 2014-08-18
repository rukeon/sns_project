#-*- coding:utf-8 -*-
from application import app
from flask import render_template, request, redirect, url_for, session
from application.models.schema import *
from application.models import user_manager


@app.route('/write')
def write() :
	return render_template('write.html')

@app.route('/write_submit', methods = ['POST', 'GET'])
def write_submit() :
	if request.method == 'POST':
		user_manager.add_write(request.form)
		return render_template('write.html')
	else:
		return	render_template('write.html')

@app.route('/write_update', methods = ['POST', 'GET'])
def write_update() :
	if request.method == 'POST':
		user_manager.update_write(request.form)
		return redirect(url_for('contents', wall_id = session['wall_id']))
	else:
		return	render_template('write.html')


@app.route('/write_comment', methods = ['POST', 'GET'])
def write_comment():
	if request.method == 'POST':
		
		user_manager.add_comment(request.form)
		return redirect(url_for('read', wall_id = session['wall_id'] , id = session['post_id']))
	else:
		return render_template('read.html')



@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404