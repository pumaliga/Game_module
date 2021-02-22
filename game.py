import models
import exceptions
import settings


player_name = ''


def play():
    global player_name
    player_name = input('Enter your name\n')
    player = models.Player(player_name, settings.PLAYER_LIVES).score
    level = 1
    enemy = models.Enemy(level)
    while True:
        user_input = input('Введите "start" для начала игры или "help" - для просмотра доступных команд\n')
        if user_input == 'help':
            settings.show_command()
        elif user_input == 'start':
            while True:
                try:
                    player.attack(enemy)
                    player.defence(enemy)
                except exceptions.EnemyDown:
                    enemy = models.Enemy(level + 1)\


        elif user_input == 'exit':
            raise exceptions.Exit


if __name__ == '__main__':
    try:
        play()
    except exceptions.GameOver:
        current_score = exceptions.GameOver
        print('Game Over')
    finally:
        print('Good bye')
