from __future__ import unicode_literals
from django.db import models
from enum import Enum

class Upload(models.Model):

    # Note: The identifer for this upload model is created and set as a primary key automatically

    # The uploaded video file
    video_title = models.CharField(max_length=80)
    video_file = models.FileField(upload_to='videos')

    # The calculated background image
    image_title = models.CharField(max_length=80)
    image_file = models.FileField(upload_to='images')

    # The status of the job
    status = models.IntegerField(db_index=True)

    # The optional callback URL provided by the user
    callback_url = models.URLField()



class Status(Enum):
    video_recieved = 0
    processing     = 1
    image_created  = 2