import unittest
import requests
import json

class TestUploadEndpoint(unittest.TestCase):

    ENDPOINT_URL = 'http://127.0.0.1:8000/uploadendpoint/'
    #ENDPOINT_URL = 'http://backgroundimage-web.7mtct8epmu.us-west-2.elasticbeanstalk.com/uploadendpoint/'

    CALLBACK_URL = 'http://127.0.0.1:28854'


    def test_endpoint_live(self):
        response = requests.get(self.ENDPOINT_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Endpoint Live!')

    def test_only_GET_and_POST_accepted(self):
        response = requests.options(self.ENDPOINT_URL)
        self.assertEqual(response.status_code, 405)
        response = requests.put(self.ENDPOINT_URL)
        self.assertEqual(response.status_code, 405)

    def test_video_empty_callback(self):
        files = {'file': open('testdata/38-20160416T131619.832823Z.mp4', 'rb')}
        response = requests.post(self.ENDPOINT_URL, files=files)
        self.assertEqual(response.status_code, 202)

    def test_video_with_callback(self):
        params = {'callback_url': self.CALLBACK_URL}
        files = {'file': open('testdata/38-20160416T131619.832823Z.mp4', 'rb')}
        response = requests.post(self.ENDPOINT_URL, files=files, json=json.dumps(params))
        self.assertEqual(response.status_code, 202)

if __name__ == '__main__':
    unittest.main()