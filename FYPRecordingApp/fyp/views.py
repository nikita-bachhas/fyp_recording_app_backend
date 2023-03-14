from django.shortcuts import render
from rest_framework import viewsets
from .models import UserRegistration, PrerecordedRecordings, PrerecordedRecordingsImitations, LiveRecordingsImitations
from .serializers import UserRegistrationSerializer, PrerecordedRecordingsSerializer, PrerecordedRecordingsImitationsSerializer, LiveRecordingsImitationsSerializer

# Create your views here.

class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer

class PrerecordedRecordingsViewSet(viewsets.ModelViewSet):
    queryset = PrerecordedRecordings.objects.all()
    serializer_class = PrerecordedRecordingsSerializer

class PrerecordedRecordingsImitationsViewSet(viewsets.ModelViewSet):
    queryset = PrerecordedRecordingsImitations.objects.all()
    serializer_class = PrerecordedRecordingsImitationsSerializer

class LiveRecordingsImitationsViewSet(viewsets.ModelViewSet):
    queryset = LiveRecordingsImitations.objects.all()
    serializer_class = LiveRecordingsImitationsSerializer