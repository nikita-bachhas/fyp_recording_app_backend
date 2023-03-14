from rest_framework import serializers
from .models import UserRegistration, PrerecordedRecordings, PrerecordedRecordingsImitations, LiveRecordingsImitations

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['UserID', 'FullName', 'EmailAddress', 'Username', 'Password']

class PrerecordedRecordingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrerecordedRecordings
        fields = ['BeatID', 'BeatName', 'Duration', 'LeftArray','RightArray', 'LeftPattern', 'RightPattern', 'Tempo']

class PrerecordedRecordingsImitationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrerecordedRecordingsImitations
        fields = ['ImitationID', 'DateofAttempt', 'TimeofAttempt', 'ImitationDuration', 'ImitationLeftArray', 'ImitationRightArray', 'ImitationTempo', 'TempoSimilarity', 'BeatsSimilarity', 'ImitationScore']

class LiveRecordingsImitationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveRecordingsImitations
        fields = ['LiveRecordingID', 'LiveRecordingImitationID', 'TimeofAttemptofOriginalBeat', 'OriginalDuration', 'OriginalLeftArray', 'OriginalRightArray', 'OriginalTempo', 'DateofAttemptofImitaionBeat', 
                  'TimeofAttemptofImitaionBeat', 'ImitationDuration', 'ImitationLeftArray', 'ImitationRightArray', 'ImitationTempo', 'TempoSimilarity', 'BeatsSimilarity', 'ImitationScore']