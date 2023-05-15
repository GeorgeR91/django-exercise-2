from rest_framework import serializers
from web.models import JobOffer


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobOffer
    fields = '__all__'
