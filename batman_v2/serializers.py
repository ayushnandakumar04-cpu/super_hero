from rest_framework import serializers
from batman.models import Superhero

class SuperheroSerializer(serializers.Serializer):

    id=serializers.IntegerField(read_only=True)

    name=serializers.CharField()

    power=serializers.ChoiceField(choices=Superhero.POWER_OPTIONS)

    team=serializers.ChoiceField(choice=Superhero.TEAM_OPTIONS)

    age=serializers.IntegerField()

    city=serializers.CharField()
    
    real_name=serializers.CharField()