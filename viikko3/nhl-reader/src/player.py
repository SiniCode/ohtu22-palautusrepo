class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    def __str__(self):
        player = f"{self.name} ({self.team})"
        points = self.goals + self.assists
        return f"{player:<30}{self.goals:>2} + {self.assists:<2} = {points}"
