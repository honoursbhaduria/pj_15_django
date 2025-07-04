from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class GFGSerailizer(serializers.ModelSerializer):
    class Meta:
        model = GFG
        fields = ['name',]

class ItemSerializer(serializers.ModelSerializer):
    gfg = GFGSerailizer()

    class Meta:
        model = Item
        fields = '__all__'
        depth = 1

        