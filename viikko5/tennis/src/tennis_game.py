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
        score = {
            "0-0": "Love-All",
            "1-1": "Fifteen-All",
            "2-2": "Thirty-All",
            "3-3": "Forty-All",
            "4-4 or higher": "Deuce"
        }

        if self.player1_score == 0:
            return score["0-0"]

        if self.player1_score == 1:
            return score["1-1"]

        if self.player1_score == 2:
            return score["2-2"]

        if self.player1_score == 3:
            return score["3-3"]

        return score["4-4 or higher"]

    def player1_is_winning_and_has_at_least_four_points(self):
        return self.player1_score > self.player2_score and self.player1_score >= 4

    def player2_is_winning_and_has_at_least_four_points(self):
        return self.player2_score > self.player1_score and self.player2_score >= 4

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

    def get_score(self):
        if self.game_is_even():
            score = self.get_even_score()

        elif self.player1_is_winning_and_has_at_least_four_points():
            difference = self.player1_score - self.player2_score
            if difference == 1:
                score = f"Advantage {self.player1_name}"
            else:
                score = f"Win for {self.player1_name}"

        elif self.player2_is_winning_and_has_at_least_four_points():
            difference = self.player2_score - self.player1_score
            if difference == 1:
                score = f"Advantage {self.player2_name}"
            else:
                score = f"Win for {self.player2_name}"

        else:
            score = self.get_scores_under_four_points()

        return score
