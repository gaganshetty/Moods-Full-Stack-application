from rest_framework import serializers
from api.models import Moodlog, Mood, Action


class MoodLogSerializer(serializers.ModelSerializer):

	class Meta:
		model = Moodlog
		fields = '__all__'
		depth = 1 #depth is used to get the foriegn key value instead of the ID

class MoodSerializer(serializers.ModelSerializer):

	class Meta:
		model = Mood
		fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Action
		fields = '__all__'