"""
API endpoint for posting a video for background image extraction

Supports:
    GET
        returns status 200

    POST
        file: <video>
        returns the job id

"""

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from models import Upload, Status




@csrf_exempt
def upload_video(request):
    if request.method == 'POST':
        try:

            callback_url = ''  # for now

            # Create and populate a new model object
            upload = Upload(video_title=request.FILES['file'].name,
                            video_file=request.FILES['file'],
                            image_title='',
                            image_file=None,
                            status=Status.video_recieved.value,
                            callback_url=callback_url)  # For now

            upload.save()

            return HttpResponse(upload.id, status=202)
        except Exception:
            return HttpResponseBadRequest('Malformed data.')

    return HttpResponseNotAllowed('Only POST allowed.')