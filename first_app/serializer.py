from rest_framework import serializers
from .models import Input

class InputSerializers(serializers.ModelSerializer):
    class meta:
        model=Input
        fields ='__all__'