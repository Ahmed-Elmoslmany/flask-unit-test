from flask import jsonify, request
from app import app
from models.post import Post
from controllers import post_controller

@app.route('/posts')
def get_posts():
    response = post_controller.get_posts()
    return response

@app.route('/posts', methods=['POST'])
def add_post():
    response = post_controller.create_post()
    return response

@app.route('/posts/<int:id>')
def get_post(id):
    response = post_controller.get_post(id)
    return response

@app.route('/posts/<int:id>', methods=['PATCH'])
def edit_post(id):
    response = post_controller.edit_post(id)
    return response

@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    response = post_controller.delete_post(id)
    return response

# Add comment to post
@app.route('/posts/<int:id>/comments', methods=['POST'])
def attach_comment_to_post(id):
    response = post_controller.attach_comment_to_post(id)
    return response

@app.route('/posts/<int:id>/tags', methods=['POST'])
def attach_tag_to_post(id):
    response = post_controller.attach_tag_to_post(id)
    return response