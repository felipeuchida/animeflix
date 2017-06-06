from django.contrib import admin
from .models import Series, Episode, Link

admin.site.register(Series)
admin.site.register(Episode)
admin.site.register(Link)