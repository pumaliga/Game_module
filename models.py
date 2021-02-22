import random
import exceptions


class Enemy:

    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise exceptions.EnemyDown


class Player:

    score = 0

    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            print('Your scores: {}'.format(self.score))
            raise exceptions.GameOver

    @staticmethod
    def fight(attack, defense):
        if (attack == 1 and defense == 2) or (attack == 2 and defense == 3) or (attack == 3 and defense == 1):
            return 1
        elif attack == defense:
            return 0
        else:
            return -1

    def attack(self, enemy_obj):
        user_input = int(input('Кем атаковать?: 1 - Маг, 2 - Воин, 3 - Разбойник\n'))
        enemy_input = enemy_obj.select_attack()
        fight_play = self.fight(user_input, enemy_input)
        if fight_play == 0:
            print("It's a draw!")
        elif fight_play == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
            self.score += 1
        elif fight_play == -1:
            print("You missed!")

    def defence(self, enemy_obj):
        enemy_input = enemy_obj.select_attack()
        user_input = int(input('Кем защищаемся?: 1 - Маг, 2 - Воин, 3 - Разбойник\n'))
        fight_play = self.fight(enemy_input, user_input)
        if fight_play == 0:
            print("It's a draw!")
        elif fight_play == 1:
            self.decrease_lives()
            print("You missed!")
        elif fight_play == -1:
            print("You defended yourself!")
