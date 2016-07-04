"""
API endpoint for polling if the video has been processed yet

Supports:
    GET
        returns status 202 if processing hasn't been finished
        returns status 200 if processing is complete

"""

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from models import Upload, Status


@csrf_exempt
def poll_for_image(request):
    if request.method == 'GET':

        try:
            id = request.GET['id']
            upload = Upload(id=id)

            if upload.status == Status.image_created.value:
                return HttpResponse(status=200)  # Processing has completed

            return HttpResponse(status=202)  # Processing has not yet completed

        except Exception:
            return HttpResponseBadRequest('You must provide an id to poll')

    return HttpResponseNotAllowed('Only GET allowed.')