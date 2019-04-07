from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Mood, Action, Moodlog
from api.serializers import MoodSerializer, ActionSerializer, MoodLogSerializer

class MoodViewSet(viewsets.ModelViewSet):

	queryset = Mood.objects.all()
	serializer_class = MoodSerializer

class ActionViewSet(viewsets.ModelViewSet):

	queryset = Action.objects.all()
	serializer_class = ActionSerializer

class MoodLogViewSet(viewsets.ModelViewSet):

	queryset = Moodlog.objects.all()
	serializer_class = MoodLogSerializer