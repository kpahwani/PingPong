from django.db import models
# Create your models here.


class Players(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    array_length = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    @staticmethod
    def active_players_count():
        return Players.objects.filter(is_active=True).count()

    @staticmethod
    def get_active_players():
        return Players.objects.filter(is_active=True)

    @staticmethod
    def get_player_by_id(id):
        return Players.objects.filter(id=id)

    def set_inactive(self):
        Players.objects.filter(id=self.id).update(is_active=False)


