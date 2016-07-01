from __future__ import unicode_literals
from django.db import models

class Upload(models.model):

    # The identifer for this upload is created automatically

    # The uploaded video
    video_path = models.FileField

    # The calculated background image
    image_path = models.FileField

    # The status of the job
    status = models.IntegerField(db_index=True)

    # The optional callback URL provided by the user
    callback_url = models.URLField