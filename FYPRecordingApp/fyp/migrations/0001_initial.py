# Generated by Django 4.1.7 on 2023-03-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrerecordedRecordings',
            fields=[
                ('BeatID', models.BigAutoField(primary_key=True, serialize=False)),
                ('BeatName', models.CharField(max_length=256)),
                ('Duration', models.FloatField(max_length=4)),
                ('LeftArray', models.IntegerField()),
                ('RightArray', models.IntegerField()),
                ('LeftPattern', models.IntegerField()),
                ('RightPattern', models.IntegerField()),
                ('Tempo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('UserID', models.BigAutoField(primary_key=True, serialize=False)),
                ('FullName', models.CharField(max_length=256)),
                ('EmailAddress', models.CharField(max_length=256)),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PrerecordedRecordingsImitations',
            fields=[
                ('ImitationID', models.BigAutoField(primary_key=True, serialize=False)),
                ('DateofAttempt', models.DateField(auto_now=True)),
                ('TimeofAttempt', models.TimeField(auto_now=True)),
                ('ImitationDuration', models.FloatField(max_length=4)),
                ('ImitationLeftArray', models.IntegerField()),
                ('ImitationRightArray', models.IntegerField()),
                ('ImitationTempo', models.IntegerField()),
                ('TempoSimilarity', models.IntegerField()),
                ('BeatsSimilarity', models.IntegerField()),
                ('ImitationScore', models.IntegerField()),
                ('BeatID', models.ManyToManyField(to='fyp.prerecordedrecordings')),
                ('UserID', models.ManyToManyField(to='fyp.userregistration')),
            ],
        ),
        migrations.CreateModel(
            name='LiveRecordingsImitations',
            fields=[
                ('LiveRecordingID', models.BigAutoField(primary_key=True, serialize=False)),
                ('LiveRecordingImitationID', models.IntegerField()),
                ('DateofAttemptofOriginalBeat', models.DateField(auto_now=True)),
                ('TimeofAttemptofOriginalBeat', models.TimeField(auto_now=True)),
                ('OriginalDuration', models.FloatField(max_length=4)),
                ('OriginalLeftArray', models.IntegerField()),
                ('OriginalRightArray', models.IntegerField()),
                ('OriginalTempo', models.IntegerField()),
                ('DateofAttemptofImitaionBeat', models.DateField(auto_now=True)),
                ('TimeofAttemptofImitaionBeat', models.TimeField(auto_now=True)),
                ('ImitationDuration', models.FloatField(max_length=4)),
                ('ImitationLeftArray', models.IntegerField()),
                ('ImitationRightArray', models.IntegerField()),
                ('ImitationTempo', models.IntegerField()),
                ('TempoSimilarity', models.IntegerField()),
                ('BeatsSimilarity', models.IntegerField()),
                ('ImitationScore', models.IntegerField()),
                ('UserID', models.ManyToManyField(to='fyp.userregistration')),
            ],
            options={
                'unique_together': {('LiveRecordingID', 'LiveRecordingImitationID')},
            },
        ),
    ]
