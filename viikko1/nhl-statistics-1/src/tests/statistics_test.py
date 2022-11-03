import unittest
from statistics import Statistics, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

def players_are_equal(player1, player2):
    if player1.name != player2.name or player1.team != player2.team or player1.goals != player2.goals or player1.assists != player2.assists:
        return False
    
    return True

def player_lists_are_equal(list1, list2):
    if len(list1) != len(list2):
        return False

    for index in range(len(list1)):
        if not players_are_equal(list1[index], list2[index]):
            return False

    return True

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_constructor_creates_statistics_with_correct_players(self):
        players1 = self.statistics._players
        players2 = [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

        self.assertTrue(player_lists_are_equal(players1, players2))

    def test_search_returns_correct_player(self):
        player1 = self.statistics.search("Kurri")
        player2 = Player("Kurri", "EDM", 37, 53)

        self.assertTrue(players_are_equal(player1, player2))

    def test_search_returns_none_if_name_not_in_player_list(self):
        player = self.statistics.search("Jari")

        self.assertIsNone(player)

    def test_team_returns_correct_list(self):
        team1 = self.statistics.team("EDM")
        team2 = [
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri", "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89)
        ]

        self.assertTrue(player_lists_are_equal(team1, team2))

    def test_top_returns_correct_list_without_key(self):
        top3a = self.statistics.top(2)
        top3b = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56)
        ]

        self.assertTrue(player_lists_are_equal(top3a, top3b))

    def test_top_returns_correct_list_by_points(self):
        top3a = self.statistics.top(2, SortBy.POINTS)
        top3b = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56)
        ]

        self.assertTrue(player_lists_are_equal(top3a, top3b))

    def test_top_returns_correct_list_by_goals(self):
        top3a = self.statistics.top(2, SortBy.GOALS)
        top3b = [
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
            Player("Kurri", "EDM", 37, 53)
        ]

        self.assertTrue(player_lists_are_equal(top3a, top3b))

    def test_top_returns_correct_list_by_assists(self):
        top3a = self.statistics.top(2, SortBy.ASSISTS)
        top3b = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Yzerman", "DET", 42, 56),
            Player("Lemieux", "PIT", 45, 54)
        ]

        self.assertTrue(player_lists_are_equal(top3a, top3b))