PLAYER_LIVES = 2
# SCORE = 0
COMMAND = ['help - выводит список возможных команд',
           'show scores - выводит записи из файл scores.txt',
           'exit - вызывает исключение и завершает работу программы']


def show_command():
    for i in COMMAND:
        print(i)

