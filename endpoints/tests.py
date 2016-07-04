import unittest
import requests

class TestUploadEndpoint(unittest.TestCase):

    # Development
    VIDEO_UPLOAD_URL = 'http://127.0.0.1:8000/uploadvideo/'
    POLL_URL = 'http://127.0.0.1:8000/poll/'

    # Production
    #VIDEO_UPLOAD_URL = 'http://backgroundimage-web.7mtct8epmu.us-west-2.elasticbeanstalk.com/uploadvideo/'
    #POLL_URL = 'http://backgroundimage-web.7mtct8epmu.us-west-2.elasticbeanstalk.com/poll/'

    def test_can_only_POST_to_upload_URL(self):
        response = requests.get(self.VIDEO_UPLOAD_URL)
        self.assertEqual(response.status_code, 405)
        response = requests.options(self.VIDEO_UPLOAD_URL)
        self.assertEqual(response.status_code, 405)
        response = requests.put(self.VIDEO_UPLOAD_URL)
        self.assertEqual(response.status_code, 405)

    def test_can_only_GET_from_poll_URL(self):
        response = requests.post(self.POLL_URL)
        self.assertEqual(response.status_code, 405)
        response = requests.options(self.POLL_URL)
        self.assertEqual(response.status_code, 405)
        response = requests.put(self.POLL_URL)
        self.assertEqual(response.status_code, 405)


    def test_upload_video(self):
        files = {'file': open('testdata/38-20160416T131619.832823Z.mp4', 'rb')}
        response = requests.post(self.VIDEO_UPLOAD_URL, files=files)
        self.assertEqual(response.status_code, 202)
        self.assertTrue(response.content > 0)  # Check for a job id

    def test_poll_for_image(self):
        files = {'file': open('testdata/38-20160416T131619.832823Z.mp4', 'rb')}
        response = requests.post(self.VIDEO_UPLOAD_URL, files=files)
        id = response.content
        response = requests.get(self.POLL_URL, {'id': id})
        self.assertTrue(response.status_code == 202 or 200)

if __name__ == '__main__':
    unittest.main()