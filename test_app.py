import unittest
from app import app, db

class BookTestCase(unittest.TestCase):
    def setUp(self):
         app.config['TESTING'] = True
         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rest.db'

         self.client = app.test_client()
         with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_book(self):
        response = self.client.post(
            '/books',
            json={
                'title': 'Test Book',
                'author': 'Test Author',
                'genre': 'Test Genre'
            }
        )        
        self.assertEqual(201, response.status_code)
        self.assertEqual(b'Book created', response.data)
        