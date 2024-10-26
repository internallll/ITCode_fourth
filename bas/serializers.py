from rest_framework import serializers
from bas import models
from bas.models import BusPark, Bus


class BusPark(serializers.ModelSerializer):
    employers = serializers.SerializerMethodField()

    def get_employers(self, obj):
        return obj.employers.name



    class Meta:
        model = BusPark
        fields = '__all__'


class Bus(serializers.ModelSerializer):
    busPark = BusPark(read_only=True)
    busPark_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Bus
        fields = '__all__'
