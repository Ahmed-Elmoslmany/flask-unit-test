import app
import controllers.posts as posts

@app.route('/posts')
def get_posts():
    return posts.get_posts()

@app.route('/posts', methods=['POST'])
def add_post():
    return posts.create_post()

@app.route('/posts/<int:id>')
def get_post(id):
    return posts.get_post(id)

@app.route('/posts/<int:id>', methods=['PATCH'])
def edit_post(id):
    return posts.edit_post(id)

@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    return posts.delete_post(id)

@app.route('/posts/<int:id>/comments', methods=['POST'])
def attach_comment_to_post(id):
    return posts.attach_comment_to_post(id)

@app.route('/posts/<int:id>/tags', methods=['POST'])
def attach_tag_to_post(id):
    return posts.attach_tag_to_post(id)