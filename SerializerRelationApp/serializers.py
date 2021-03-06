from dataclasses import field
from pyexpat import model
from .models import Singer,Song
from rest_framework import serializers





class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']

class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True)
    # song = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Song-detail')
    # song = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
    song = serializers.HyperlinkedIdentityField(view_name='Song-detail')
    class Meta:
        model = Singer
        fields = ['id','name','gender','song']

