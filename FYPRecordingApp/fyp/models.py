from django.db import models

# Create your models here.

class UserRegistration(models.Model):
    UserID = models.BigAutoField(primary_key=True)
    FullName = models.CharField(max_length=256)
    EmailAddress = models.CharField(max_length=256)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

class PrerecordedRecordings(models.Model):
    BeatID = models.BigAutoField(primary_key=True)
    BeatName = models.CharField(max_length=256)
    Duration = models.FloatField(max_length=4)
    LeftArray = models.IntegerField()
    RightArray = models.IntegerField()
    LeftPattern = models.IntegerField()
    RightPattern = models.IntegerField()
    Tempo = models.IntegerField()

class PrerecordedRecordingsImitations(models.Model):
    ImitationID = models.BigAutoField(primary_key=True)
    DateofAttempt = models.DateField(auto_now=True)
    TimeofAttempt = models.TimeField(auto_now=True)
    ImitationDuration = models.FloatField(max_length=4)
    ImitationLeftArray = models.IntegerField()
    ImitationRightArray = models.IntegerField()
    ImitationTempo = models.IntegerField()
    TempoSimilarity = models.IntegerField()
    BeatsSimilarity = models.IntegerField()
    ImitationScore = models.IntegerField() 
    UserID = models.ManyToManyField(UserRegistration)
    BeatID = models.ManyToManyField(PrerecordedRecordings)

class LiveRecordingsImitations(models.Model):
    LiveRecordingID = models.BigAutoField(primary_key=True)
    LiveRecordingImitationID = models.IntegerField()
    DateofAttemptofOriginalBeat = models.DateField(auto_now=True)
    TimeofAttemptofOriginalBeat = models.TimeField(auto_now=True)
    OriginalDuration = models.FloatField(max_length=4)
    OriginalLeftArray = models.IntegerField()
    OriginalRightArray = models.IntegerField()
    OriginalTempo = models.IntegerField()
    DateofAttemptofImitaionBeat = models.DateField(auto_now=True)
    TimeofAttemptofImitaionBeat = models.TimeField(auto_now=True)
    ImitationDuration = models.FloatField(max_length=4)
    ImitationLeftArray = models.IntegerField()
    ImitationRightArray = models.IntegerField()
    ImitationTempo = models.IntegerField()
    TempoSimilarity = models.IntegerField()
    BeatsSimilarity = models.IntegerField()
    ImitationScore = models.IntegerField() 
    UserID = models.ManyToManyField(UserRegistration)
    
    class Meta:
        unique_together = (("LiveRecordingID", "LiveRecordingImitationID"),)