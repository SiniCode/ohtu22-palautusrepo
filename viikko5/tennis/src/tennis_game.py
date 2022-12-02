class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def game_is_even(self):
        return self.player1_score == self.player2_score

    def get_even_score(self):
        even_score = {
            "0-0": "Love-All",
            "1-1": "Fifteen-All",
            "2-2": "Thirty-All",
            "3-3": "Forty-All",
            "4-4 or higher": "Deuce"
        }

        if self.player1_score == 0:
            score = even_score["0-0"]

        elif self.player1_score == 1:
            score = even_score["1-1"]

        elif self.player1_score == 2:
            score = even_score["2-2"]

        elif self.player1_score == 3:
            score = even_score["3-3"]

        else:
            score = even_score["4-4 or higher"]

        return score

    def both_players_have_under_four_points(self):
        return self.player1_score < 4 and self.player2_score < 4

    def get_scores_under_four_points(self):
        score = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

        player1_score = score[self.player1_score]
        player2_score = score[self.player2_score]

        return f"{player1_score}-{player2_score}"

    def player1_is_leading(self):
        return self.player1_score > self.player2_score

    def get_score_with_leading_player(self, player_name):
        difference = self.player1_score - self.player2_score
        if abs(difference) == 1:
            score = f"Advantage {player_name}"
        else:
            score = f"Win for {player_name}"

        return score

    def get_score(self):
        if self.game_is_even():
            score = self.get_even_score()

        elif self.both_players_have_under_four_points():
            score = self.get_scores_under_four_points()

        elif self.player1_is_leading():
            score = self.get_score_with_leading_player(self.player1_name)
        
        else:
            score = self.get_score_with_leading_player(self.player2_name)

        return score
