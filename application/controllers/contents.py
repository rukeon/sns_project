#-*- coding:utf-8 -*-
from application import app
from flask import render_template, session, redirect, url_for,request
from application.models import user_manager
import json

@app.route('/', defaults={'wall_id':0}) 
@app.route('/contents/<int:wall_id>')
def contents(wall_id):
	if wall_id == 0:
		session['username'] = session['email']
		session['wall_id'] = wall_id
		return render_template('contents.html')
	else:		
		
		wall_user = user_manager.get_user(wall_id)
		session['wall_id'] = wall_id
		session['username'] = wall_user.username
		# post_lists = wall_user.wall_posts
		post_lists = user_manager.get_wall_posts(session['wall_id'])
		return render_template('contents.html', post_lists = post_lists)

@app.route('/get_posts', methods=['POST', 'GET'])
def get_posts():
	if request.method == 'POST':
		# posts = user_manager.get_wall_posts(session['wall_id'])
		# return	render_template('wall_ajax.html', posts = posts, wall_id = session['wall_id'])
		posts = user_manager.get_wall_posts(session['wall_id'],request.form['number'])
		return render_template('wall_ajax.html', posts = posts)
	# if posts.count() == 0:
	#    return ''
	else:
		return render_template('wall_ajax.html')

# @app.route('/add_contents', methods = ['POST','GET'])
# def add_contents():
# 	if request.method == 'POST':
# 		posts = user_manager.get_post_by_wall_id(session['wall_id'])
# 	return	render_template('wall_ajax.html', posts = posts, wall_id = session['wall_id'])



@app.route('/delete/<int:id>')
def delete(id):
	check_id = user_manager.get_post(id)
	if check_id.user_id == session['user_id']:
		
		user_manager.delete_contents_body(id)
		return redirect(url_for('contents', wall_id = check_id.wall_id))
	else:
		alert = "you can't delete!"
		return render_template("cannot_delete.html", alert = alert)

@app.route('/revise/<int:id>')
def revise(id):
	check_id = user_manager.get_post(id)
	if check_id.user_id == session['user_id']:
				
		return render_template('post_revise.html', check_id = check_id)
	else:
		alert = "you can't revise!"
		return render_template("cannot_delete.html", alert = alert)


@app.route('/delete_comments/<int:id>')
def delete_comments(id):
	find_id = user_manager.get_comment(id)
	if find_id.user_id == session['user_id']:
		
		user_manager.delete_comments_body(id)
		return redirect(url_for('read', wall_id = session['wall_id'], id = session['post_id'] ))
	else:
		alert = "you can't delete!"
		return render_template("cannot_delete.html", alert = alert)


@app.route('/read/<int:wall_id>/<int:id>')
def read(wall_id, id):
	check_post = user_manager.get_post(id)
	session['post_id'] = id
	comment_lists = check_post.comments	
	return render_template('read.html', check_post = check_post, comment_lists = comment_lists)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404