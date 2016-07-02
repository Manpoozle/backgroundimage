"""
API endpoint for posting a video for background image extraction

{
  "file: "<url to video>"
  "callback_url": "<url to be notified when processing is done>" // Optional
}

"""
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def upload_video(request):
    if request.method == 'GET':
        return HttpResponse("Endpoint Live!")

    elif request.method == 'POST':
        try:
            print request.body
            return HttpResponse(status=202)
        except Exception:
            return HttpResponseBadRequest('Malformed data.')

    return HttpResponseNotAllowed('Only GET and POST allowed.')