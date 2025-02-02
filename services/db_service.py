from app import db
from models.model import Post, Comment, Tag

class DBService():
    @staticmethod
    def get_post(post_id):
        return Post.query.get(post_id)
    
    @staticmethod
    def get_all_posts():
        return Post.query.all()
    
    @staticmethod
    def create_post(content):
        new_post = Post(content=content)
        db.session.add(new_post)
        db.session.commit()
        return new_post
    
    @staticmethod
    def update_post(post, content):
        post.content = content
        db.session.commit()
        return post
    
    @staticmethod
    def delete_post(post):
        db.session.delete(post)
        db.session.commit()

    @staticmethod
    def add_comment_to_post(text, post_id):
        new_comment = Comment(text=text, post_id=post_id)
        db.session.add(new_comment)
        db.session.commit()
        return new_comment
    
    @staticmethod
    def add_tag_to_post(title, post):
        tag = Tag.query.filter(title=title).first()
        if not tag:
            tag = Tag(title=title)
            db.session.add(tag)
            db.session.commit()

        post.tags.append(tag)
        db.session.commit()
        return tag            