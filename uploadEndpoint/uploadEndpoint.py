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
import os

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from models import Upload, Status
from ebdjango import settings

@csrf_exempt
def upload_video(request):
    if request.method == 'GET':
        return HttpResponse("Endpoint Live!")

    elif request.method == 'POST':
        body = request.body # This is important! django will prematurely close the connection if the POST buffer is not consumed!
        callback_url = None # for now

        # Create and populate a new model object
        upload = Upload(video_title=request.FILES['file'].name,
                        video_file=request.FILES['file'],
                        image_title=None,
                        image_file=None,
                        status=Status.video_recieved.value,
                        callback_url=callback_url) # For now

        # Save the file corresponding to our new model object
        save_uploaded_video(request.FILES['file'])

        upload.save()

        try:
            # print request.FILES
            # print request.FILES.getlist('file')[0]
            # if ('file' in request.FILES):
            #     upload = Upload(video=('somename', request.FILES.getlist('file')[0]))
            #     print type(upload.video)

                # upload = Upload(video=request.FILES.getlist('file')[0],
                #                 image=None,
                #                 status=Status.video_recieved,
                #                 callback_url=None)

            return HttpResponse(status=202)
        except Exception:
            return HttpResponseBadRequest('Malformed data.')

    return HttpResponseNotAllowed('Only GET and POST allowed.')


def save_uploaded_video(file):

    destinationDir = os.path.join(settings.BASE_DIR, 'videos')
    destination = os.path.join(destinationDir, file.name)

    with open(destination, 'wb+') as destination_file:
        for chunk in file.chunks():
            destination_file.write(chunk)