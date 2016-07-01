import unittest
import requests

class TestUploadEndpoint(unittest.TestCase):

    ENDPOINT_URL = 'http://127.0.0.1:8000/uploadendpoint/'


    def test_endpoint_live(self):
        response = requests.get(self.ENDPOINT_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Endpoint Live!')

    def test_only_GET_and_POST_accepted(self):
        response = requests.options(self.ENDPOINT_URL)
        self.assertEqual(response.status_code, 400)

    def test_video_no_callback(self):
        response = requests.post(self.ENDPOINT_URL, json={'file': 'somepath', 'callbackurl' : ''})
        self.assertEqual(response.content,'')

if __name__ == '__main__':
    unittest.main()