class GameOver(Exception):

    @staticmethod
    def save_score(name, scores):
        with open('scores.txt', 'a') as save_score:
            save_score.write(f"Name: {name}, Scores: {scores}\n")


class EnemyDown(Exception):
    pass


class Score:

    def __init__(self):
        with open('scores.txt') as file:
            lines = [line.split('Scores: ') for line in file]
            result = open("scores.txt", 'w')

            for line in sorted(lines, key=lambda x: int(x[1]), reverse=True)[:10]:
                result.write('Scores: '.join(line))


class Exit(Exception):
    pass

