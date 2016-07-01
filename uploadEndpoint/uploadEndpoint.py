"""
API endpoint for posting a video for background image extraction

{
  "file: "<url to video>"
  "callback_url": "<url to be notified when processing is done>" // Optional
}

"""
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def upload_video(request):
    if request.method == 'GET':
        return HttpResponse("Endpoint Live!")

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            for x in data:
                print x
        except KeyError:
            HttpResponseBadRequest('Malformed json.')

    return HttpResponseBadRequest()