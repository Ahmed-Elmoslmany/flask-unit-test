from app import db
from flask import jsonify, request
from http import HTTPStatus
from models.post import Post
from models.comment import Comment
from models.tag import Tag


def get_posts():
    posts = Post.query.all()
    posts_data = []

    if not posts:
        return jsonify({
            "status": "Fail",
            "data": {
                "message": "Not posts found"
            }
        }, HTTPStatus.NOT_FOUND)

    for post in posts:
        comments = [{"id": comment.id, "text": comment.text} for comment in post.comments]
        tags = [{"id": tag.id, "title": tag.title} for tag in post.tags]

        posts_data.append({
            "id": post.id,
            "content": post.content,
            "comments": comments,
            "tags": tags
        })

    return jsonify({
        "status": "success",
        "total": len(posts_data),
        "data": posts_data
    }, HTTPStatus.OK)

def get_post(post_id):
    post = Post.query.get(post_id)

    if not post:
        return jsonify({
            "status": "Fail",
            "data": {
                "message": "No post found"
            }
        }, HTTPStatus.NOT_FOUND)

    comments = [{"id": comment.id, "text": comment.text} for comment in post.comments]
    tags = [{"id": tag.id, "title": tag.title} for tag in post.tags]


    return jsonify({
        "status": "success",
        "data": {
            "id": post.id,
            "content": post.content,
            "comments": comments,
            "tags": tags
        }
    }, HTTPStatus.OK)

def create_post():
    data = request.get_json()
    print(data)

    if not data or not 'content' in data:
        return jsonify({
            "status": "Fail",
            "data": {
                "message": "Content is required"
            }
        }, HTTPStatus.BAD_REQUEST)
    
    new_post = Post(content=data['content'])
    db.session.add(new_post)
    db.session.commit()

    return jsonify({
        "status": "success",
        "data": {
            "id": new_post.id,
            "conent": new_post.content
        }
    }, HTTPStatus.OK)

def edit_post(post_id):
    data = request.get_json()

    if not data or not 'content' in data:
        return jsonify({
            "status": "Fail",
            "data": {
                "message": "Content is required"
            }
        }, HTTPStatus.BAD_REQUEST)
    
    post = Post.query.get(post_id)

    if not post:
        return jsonify({
            "status": "Fail",
            "data": {
                "message": "No post found"
            }
        }, HTTPStatus.NOT_FOUND)
    
    post.content = data['content']
    db.session.commit()

    return jsonify({
        "status": "success",
        "data": {
            "id": post.id,
            "conent": data['content']
        }
    }, HTTPStatus.OK)

def delete_post(post_id):
    post = Post.query.get(post_id)
    
    if not post:
        return jsonify({
            "status": "Fail",
            "data": {
                "message": f"Post with id: {id} not found"
            }
        }, HTTPStatus.NOT_FOUND)

    db.session.delete(post)
    db.session.commit()

    return jsonify({
        "status": "success",
        "data": {
            "message": f"Post with id: {id} has Deleted"
        }
    }, HTTPStatus.OK)

def attach_comment_to_post(post_id):
    comment_data = request.get_json()

    if not comment_data or not 'text' in comment_data:
        return jsonify({
            "status": "Fail",
            "data": {
                "message": "Text is required"
            }
        }, HTTPStatus.BAD_REQUEST)
    
    new_comment = Comment(text=comment_data['text'], post_id=post_id)
    db.session.add(new_comment)
    db.session.commit()

    return get_post(post_id)

def attach_tag_to_post(post_id):
    tag_data = request.get_json()
    post = Post.query.get(post_id)

    if not post:
        return jsonify({
            "status": "Fail",
            "data": {
                "message": "Not post found"
            }
        }, HTTPStatus.NOT_FOUND)

    if not tag_data or not 'title' in tag_data:
        return jsonify({
            "status": "Fail",
            "data": {
                "message": "title is required"
            }
        }, HTTPStatus.BAD_REQUEST)
    
    tag = Tag.query.filter_by(title=tag_data['title']).first()

    if not tag:
        tag = Tag(title=tag_data['title'])
        db.session.add(tag)
        db.session.commit()
    
    post.tags.append(tag)
    db.session.commit()

    return get_post(post_id)