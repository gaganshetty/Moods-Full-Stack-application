from django.contrib import admin
from api.models import Mood, Action, Moodlog
# Register your models here.
admin.site.register(Mood)
admin.site.register(Action)
admin.site.register(Moodlog)