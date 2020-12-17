from rest_framework import serializers
from .models import Player, ZScoreSet, Draft, DraftPick

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Player
        fields='__all__'

class ZScoreSetSerializer(serializers.ModelSerializer):
    class Meta:
        model=ZScoreSet
        fields='__all__'

class DraftSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        ''' If object is being updated don't allow creator to be changed. '''
        super().__init__(*args, **kwargs)
        if self.instance is not None:
            self.fields.get('creator').read_only = True
    
    class Meta:
        model=Draft
        fields='__all__'

class DraftPickSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        ''' If object is being updated don't allow draft to be changed. '''
        super().__init__(*args, **kwargs)
        if self.instance is not None:
            self.fields.get('draft').read_only = True
    
    class Meta:
        model=DraftPick
        fields='__all__'