from rest_framework import serializers
from footballapp.models import Player, Team
# from footballapp.serializers import PlayerSerializer, TeamSerializer

class PlayerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Player
		fields = ('id', 'Name', 'Age', 'Club', 'Position', 'Birthdate', 'Nationality','InfoId')
class TeamSerializer(serializers.ModelSerializer):
	Player_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True, default='')
	class Meta:
		model = Team
		fields = ('id', 'TeamName', 'League','Player_id')
        


