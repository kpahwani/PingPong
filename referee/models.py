from math import log
from django.db import models
from players.models import Players
from random import shuffle, sample, randint
from collections import OrderedDict
# Create your models here.


class Championships(models.Model):
    id = models.AutoField(primary_key=True)
    winner = models.ForeignKey(Players, related_name='winner', on_delete=models.CASCADE, null=True)

    @staticmethod
    def validate_championship():
        if Players.active_players_count() == 8:
            return True
        else:
            return False

    @staticmethod
    def get_random_pair(active_players):
        shuffle(active_players)
        return active_players.pop(0), active_players.pop()

    @staticmethod
    def get_championships_list():
        return list(Championships.objects.values_list('id', flat=True))

    def set_winner(self):
        self.winner = Players.objects.filter(is_active=True).first()
        self.winner.set_inactive()
        self.save()

    def start_championship(self):
        if self.validate_championship():
            active_players = Players.active_players_count()
            league_count = int(log(active_players, 2))
            for i in range(league_count):
                active_players = Players.active_players_count()
                game_count = int(active_players / 2)
                players_list = list(Players.get_active_players())
                for j in range(game_count):
                    p1, p2 = self.get_random_pair(players_list)
                    game = Games.objects.create(championship_id=self, player1=p1, player2=p2)
                    game.play_game()
                    game.shutdown_loser()
            self.set_winner()
            return self.winner
        else:
            return False

    @staticmethod
    def get_championship_details(pk):
        games = Games.objects.filter(championship_id=pk).order_by('id')
        result = list()
        for game in games:
            result.append(game.get_game_details())
        return result


class Games(models.Model):
    id = models.AutoField(primary_key=True)
    championship_id = models.ForeignKey(Championships, related_name='championship', on_delete=models.CASCADE,null=True)
    player1 = models.ForeignKey(Players, related_name='player_1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Players, related_name='player_2', on_delete=models.CASCADE)
    player1_points = models.IntegerField(default=0)
    player2_points = models.IntegerField(default=0)

    @staticmethod
    def initialise_game(c_id, p1_id, p2_id):
        game = Games.objects.create(championship_id=c_id, player1_id=p1_id, player2_id=p2_id)
        return game

    @staticmethod
    def get_random_array(length):
        return sample(range(1, 10), length)

    @staticmethod
    def get_random_number():
        return randint(1, 10)

    def get_winner(self):
        if self.player1_points > self.player2_points:
            return self.player1
        else:
            return self.player2

    def get_game_details(self):
        details = OrderedDict()
        details['game_id'] = self.id
        details['player1'] = self.player1.username
        details['player2'] = self.player2.username
        details['p1_score'] = self.player1_points
        details['p2_score'] = self.player2_points
        details['winner'] = self.get_winner().username
        return details

    def shutdown_loser(self):
        self.get_loser().set_inactive()

    def get_loser(self):
        if self.player2_points < self.player1_points:
            return self.player2
        else:
            return self.player1

    def update_points(self):
        Games.objects.filter(id=self.id).update(player1_points=self.player1_points, player2_points=self.player2_points)

    def play_game(self):
        offensive = self.player1
        defensive = self.player2
        off_array = self.get_random_array(offensive.array_length)
        def_array = self.get_random_array(defensive.array_length)
        off_count = 0
        def_count = 0
        while True:
            if self.get_random_number() in def_array:
                def_count += 1
            else:
                off_count += 1
            if off_count != 5 and def_count != 5:
                offensive, defensive = defensive, offensive
                off_count, def_count = def_count, off_count
                off_array, def_array = def_array, off_array
            else:
                break
        if offensive == self.player1:
            self.player1_points = off_count
            self.player2_points = def_count
        else:
            self.player1_points = def_count
            self.player2_points = off_count
        self.update_points()
