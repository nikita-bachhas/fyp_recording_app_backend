from django.contrib import admin
from .models import UserRegistration, PrerecordedRecordings, PrerecordedRecordingsImitations, LiveRecordingsImitations

# Register your models here.

@admin.register(UserRegistration)
class UserRegistration(admin.ModelAdmin):
    list_display = ('UserID', 'FullName', 'EmailAddress', 'Username','Password')

@admin.register(PrerecordedRecordings)
class PrerecordedRecordings(admin.ModelAdmin):
    list_display = ('BeatID', 'BeatName', 'Duration', 'LeftArray','RightArray', 'LeftPattern', 'RightPattern', 'Tempo')

@admin.register(PrerecordedRecordingsImitations)
class PrerecordedRecordingsImitations(admin.ModelAdmin):
    list_display = ('ImitationID', 'DateofAttempt', 'TimeofAttempt', 'ImitationDuration','ImitationLeftArray', 'ImitationRightArray', 'ImitationTempo', 'TempoSimilarity', 'BeatsSimilarity', 'ImitationScore')

@admin.register(LiveRecordingsImitations)
class LiveRecordingsImitations(admin.ModelAdmin):
    list_display = ('LiveRecordingID', 'LiveRecordingImitationID', 'TimeofAttemptofOriginalBeat', 'OriginalDuration','OriginalLeftArray', 'OriginalRightArray', 'OriginalTempo', 'DateofAttemptofImitaionBeat', 'TimeofAttemptofImitaionBeat', 'ImitationDuration', 'ImitationLeftArray', 'ImitationRightArray', 'ImitationTempo', 'TempoSimilarity', 'BeatsSimilarity', 'ImitationScore')