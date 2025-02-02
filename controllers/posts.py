from flask import jsonify, request
from http import HTTPStatus
from services.db_service import DBService

class PostController():

    def get_posts(self):
        posts = DBService.get_all_posts()
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

    def get_post(self, post_id):
        post = DBService.get_post(post_id)

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

    def create_post(self):
        data = request.get_json()

        if not data or not 'content' in data:
            return jsonify({
                "status": "Fail",
                "data": {
                    "message": "Content is required"
                }
            }, HTTPStatus.BAD_REQUEST)
        
        new_post = DBService.create_post(data['content'])

        return jsonify({
            "status": "success",
            "data": {
                "id": new_post.id,
                "conent": new_post.content
            }
        }, HTTPStatus.OK)

    def edit_post(self, post_id):
        data = request.get_json()

        if not data or not 'content' in data:
            return jsonify({
                "status": "Fail",
                "data": {
                    "message": "Content is required"
                }
            }, HTTPStatus.BAD_REQUEST)
        
        post = DBService.get_post(post_id)

        if not post:
            return jsonify({
                "status": "Fail",
                "data": {
                    "message": "No post found"
                }
            }, HTTPStatus.NOT_FOUND)
        
        updated_post = DBService.update_post(post, data['content'])

        return jsonify({
            "status": "success",
            "data": {
                "id": updated_post.id,
                "conent": updated_post.content
            }
        }, HTTPStatus.OK)

    def delete_post(self, post_id):
        post = DBService.get_post(post_id)
        
        if not post:
            return jsonify({
                "status": "Fail",
                "data": {
                    "message": f"Post with id: {id} not found"
                }
            }, HTTPStatus.NOT_FOUND)

        DBService.delete_post(post)

        return jsonify({
            "status": "success",
            "data": {
                "message": f"Post with id: {id} has Deleted"
            }
        }, HTTPStatus.OK)

    def attach_comment_to_post(self, post_id):
        comment_data = request.get_json()

        if not comment_data or not 'text' in comment_data:
            return jsonify({
                "status": "Fail",
                "data": {
                    "message": "Text is required"
                }
            }, HTTPStatus.BAD_REQUEST)
        
        DBService.add_comment_to_post(comment_data['text'], post_id)

        return self.get_post(post_id)

    def attach_tag_to_post(self, post_id):
        tag_data = request.get_json()
        post = DBService.get_post(post_id)

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

        DBService.add_tag_to_post(tag_data['title'], post)

        return self.get_post(post_id)