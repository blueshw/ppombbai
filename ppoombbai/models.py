from django.db import models

# Create your models here.
class TUser(models.Model):
    uid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 't_user'


class TSeason(models.Model):
    uid = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    state = models.CharField(max_length=4)
    start_dt = models.DateTimeField(auto_now=True)
    end_dt = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 't_season'


class TEvent(models.Model):
    uid = models.BigIntegerField(primary_key=True)
    season_uid = models.IntegerField()
    title = models.CharField(max_length=255)
    from_user_uid = models.IntegerField()
    receive_user_uid = models.IntegerField()
    amount = models.IntegerField()
    create_dt = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 't_event'


class TSeasonResult(models.Model):
    uid = models.BigIntegerField(primary_key=True)
    season_uid = models.IntegerField()
    from_user_uid = models.IntegerField()
    to_user_uid = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = True
        db_table = 't_season_result'