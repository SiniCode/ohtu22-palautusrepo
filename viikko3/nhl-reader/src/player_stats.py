from player_reader import PlayerReader
from player import Player


class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = list(filter(lambda player : player.nationality == nationality,
                              self.reader.get_players()))

        players.sort(reverse=True, key=lambda player : player.goals + player.assists)
        return players
