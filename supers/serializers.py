from rest_framework import serializers
from .models import Supers

class SuperSerializer (serializers.ModelSerializer):
        class Meta:
            model= Supers
            field=['name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type']