from app import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    modefied = db.Column(db.Boolean)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))