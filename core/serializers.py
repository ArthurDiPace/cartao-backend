from django.core import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from core.models import *



class CartoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartoes
        fields = "__all__"

