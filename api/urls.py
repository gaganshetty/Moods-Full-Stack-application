from django.urls import path, include
# from api.views import GetAllMoods, GetAllActions, GetAllMoodlogs
from rest_framework.routers import DefaultRouter
from api.viewsets import *

router = DefaultRouter()
router.register(r'moods', MoodViewSet)
router.register(r'actions', ActionViewSet)
router.register(r'logs', MoodLogViewSet)

urlpatterns = [
	# path('moods/', GetAllMoods.as_view()),
	# path('actions/', GetAllActions.as_view()),
	# path('logs/', 'GetAllMoodlogs.as_view()),
		path('',include(router.urls))
]