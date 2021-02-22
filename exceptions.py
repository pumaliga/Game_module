class GameOver(Exception):

    # @staticmethod
    # def save_score(name, score):
    #     file = open('score.txt', 'a')
    #     file.write(f'Name: {name}, Score: {score}\n')
    #     file.close()

    def __str__(self):
        print('Game Over')


class EnemyDown(Exception):
    pass


class Score:

    def __init__(self):
        with open('score.txt') as file:
            lines = [line.split('Scores: ') for line in file]

        # for line in file(lines, key=lambda x: int(x[1]), reverse=True)[:10]:
        #     output.write('Scores: '.join(line))

class Exit(Exception):
    pass

