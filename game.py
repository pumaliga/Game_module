import models
import exceptions
from settings import PLAYER_LIVES, show_command


PLAYER_NAME = ''
SCORES = 0


def play():
    global PLAYER_NAME
    PLAYER_NAME = input('Enter your name\n')
    player = models.Player(PLAYER_NAME, PLAYER_LIVES)
    global SCORES
    SCORES = player.score
    level = 1
    enemy = models.Enemy(level)
    while True:
        user_input = input(
            'Введите "start" для начала игры или "help" - для просмотра доступных команд\n')
        if user_input == 'help':
            show_command()
        elif user_input == 'start':
            while True:
                try:
                    player.attack(enemy)
                    player.defence(enemy)
                except exceptions.EnemyDown:
                    enemy = models.Enemy(level + 1)
                    SCORES += 5

        elif user_input == 'show scores':
            with open('scores.txt', 'r') as file:
                for line in file:
                    print(line.strip())

        elif user_input == 'exit':
            raise exceptions.Exit


if __name__ == '__main__':
    try:
        play()
    except exceptions.GameOver:
        print('Game Over')
        final_score = exceptions.GameOver
        final_score.save_score(PLAYER_NAME, SCORES)
        best_scores = exceptions.Score()
    finally:
        print('Good bye')
