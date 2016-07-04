"""
API endpoint for posting a video for background image extraction

Supports:
    GET
        returns status 200

    POST
        file: <video>
        callback_url: <url to be notified when processing is done> // Optional
        returns the job id

"""
import json

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from models import Upload, Status

@csrf_exempt
def upload_video(request):
    if request.method == 'GET':
        return HttpResponse("Endpoint Live!")

    elif request.method == 'POST':
        #try:

            #print request.POST

            callback_url = ''  # for now

            # Create and populate a new model object
            upload = Upload(video_title=request.FILES['file'].name,
                            video_file=request.FILES['file'],
                            image_title='',
                            image_file=None,
                            status=Status.video_recieved.value,
                            callback_url=callback_url)  # For now

            upload.save()

            return HttpResponse(status=202)
        #except Exception:
        #    return HttpResponseBadRequest('Malformed data.')

    return HttpResponseNotAllowed('Only GET and POST allowed.')