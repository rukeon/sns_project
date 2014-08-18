from application import db
from flask import request, session
from schema import *

def add_user(data):
	user = User(
	email = data['email'],
	username = data['username'],
	gender = data['gender'],
	password = db.func.md5(data['password']),
	mobile = data['mobile'],
	birthday = data['birthday']
	)

	db.session.add(user)
	db.session.commit()


# def get_post_by_wall_id(wall_id):
# 	return	Post.query.filter(Post.wall_id == wall_id).order_by(db.desc(Post.edited_time)).limit(5)

def login_check(email, password):
	return User.query.filter(User.email == email, User.password == db.func.md5(password)).count() != 0

def get_user(wall_id):
	return User.query.filter(User.id == wall_id).one()

def get_post(id):
	return Post.query.filter(Post.id == id).one()

def get_comment(id):
	return Comment.query.filter(Comment.id == id).one()

def get_wall_posts(wall_id, number=0):
	number = int(number)

	if number == 0:
		return Post.query.filter(Post.wall_id == wall_id).order_by(db.desc(Post.edited_time)).limit(5)
	else:
		return Post.query.filter(Post.wall_id == wall_id).order_by(db.desc(Post.edited_time)).slice(number, number+5)
	

def add_write(content):
	if 'is_secret' not in content:
		post = Post(
			body = content['body'],
			is_secret = 0,
			user_id = session['user_id'],
			wall_id = session['wall_id']

			)
	else:
		post = Post(
			body = content['body'],
			is_secret = 1,
			user_id = session['user_id'],
			wall_id = session['wall_id']

			)

	db.session.add(post)
	db.session.commit()

def delete_contents_body(id):
	del_post = Post.query.get(id)
	db.session.delete(del_post)
	db.session.commit()


def delete_comments_body(id):
	del_comment = Comment.query.get(id)
	db.session.delete(del_comment)
	db.session.commit()

def update_write(data):
	post = Post.query.get(session['post_id'])
	post.body = data['body']
	db.session.commit()

def add_comment(material):
	comment = Comment(
		body = material['comment_body'],
		post_id = session['post_id'],
		user_id = session['user_id']
		)

	db.session.add(comment)
	db.session.commit()
