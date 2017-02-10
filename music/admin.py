from django.contrib import admin

from .models import Album,Song #importing album and song of models.py

admin.site.register(Album)#in order to register Album class of models.py in Admin site UI
admin.site.register(Song)
