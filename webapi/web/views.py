from django.shortcuts import render
from rest_framework import generics
from web.models import JobOffer
from api.serializers import JobSerializer


class JobList(generics.ListCreateAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobSerializer

    class JobDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = JobOffer.objects.all()
        serializer_class = JobSerializer
