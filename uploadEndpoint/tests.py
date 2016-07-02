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
        self.assertEqual(response.status_code, 405)
        response = requests.put(self.ENDPOINT_URL)
        self.assertEqual(response.status_code, 405)

    def test_video_empty_callback(self):
        files = {'file': open('testdata/38-20160416T131619.832823Z.mp4', 'rb')}
        response = requests.post(self.ENDPOINT_URL, files=files)
        self.assertEqual(response.status_code, 202)

if __name__ == '__main__':
    unittest.main()