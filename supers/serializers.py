from rest_framework import serializers
from .models import Supers

class SuperSerializer (serializers.ModelSerializer):
        class Meta:
            model= Supers
            fields = '__all__'
            field=['name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type', 'super_type_id']
            depth=1

        super_type_id=serializers.IntegerField(write_only=True)