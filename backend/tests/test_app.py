import json
from flask_testing import TestCase
from app import app

class MyTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_send_string(self):
        response = self.client.post('/reverse_string', data=json.dumps({'string': '321CbA'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'reversed_string': 'AbC123'})

if __name__ == '__main__':
    import unittest
    unittest.main()

