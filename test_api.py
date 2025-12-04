import unittest
import json
from main import predict_anxiety
from flask import Flask, Request

class TestAnxietyFunction(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

    def test_predict_low_anxiety(self):
        # Simulate a request with low scores (all 0s)
        data = {f'q{i}': 0 for i in range(1, 8)}
        data['response_time'] = 5000
        
        with self.app.test_request_context(
            method='POST',
            data=json.dumps(data),
            content_type='application/json'
        ):
            # We need to mock the request object passed to the function
            # In functions-framework, the function receives a Flask Request object
            from flask import request
            response = predict_anxiety(request)
            
            # Unpack response (it returns a tuple with body, status, headers)
            body, status, headers = response
            json_body = body.get_json()
            
            print(f"\nTest Low Anxiety: Input={data} -> Result={json_body}")
            self.assertEqual(status, 200)
            self.assertEqual(json_body['classification'], 'Low')

    def test_predict_high_anxiety(self):
        # Simulate a request with high scores (all 3s)
        data = {f'q{i}': 3 for i in range(1, 8)} # Score 21
        data['response_time'] = 2000
        
        with self.app.test_request_context(
            method='POST',
            data=json.dumps(data),
            content_type='application/json'
        ):
            from flask import request
            response = predict_anxiety(request)
            body, status, headers = response
            json_body = body.get_json()
            
            print(f"\nTest High Anxiety: Input={data} -> Result={json_body}")
            self.assertEqual(status, 200)
            self.assertEqual(json_body['classification'], 'High')

if __name__ == '__main__':
    unittest.main()
