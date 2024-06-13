from random import randint


class Soldier:
    def __init__(self, name='Noname', health=100):
        self.name = name
        self.health = health
        self.attack_type = 'рукой'  # Предполагаем, что изначально все бьют рукой

    def set_name(self, name):
        self.name = name

    def change_attack_type(self, attack_type):
        self.attack_type = attack_type

    def make_kick(self, enemy):
        if self.attack_type == 'ногой':
            enemy.health -= 20
            if enemy.health < 0:
                enemy.health = 0
            self.health += 10
            print(self.name, "бьет", enemy.name)
            print('%s = %d' % (enemy.name, enemy.health))

    def make_hit(self, enemy):
        if self.attack_type == 'рукой':
            enemy.health -= 10
            if enemy.health < 0:
                enemy.health = 0
            self.health += 5
            print(self.name, "бьет", enemy.name)
            print('%s = %d' % (enemy.name, enemy.health))

    def make_head_hit(self, enemy):
        if self.attack_type == 'головой':
            enemy.health -= 15
            if enemy.health < 0:
                enemy.health = 0
            self.health += 7
            print(self.name, "бьет", enemy.name)
            print('%s = %d' % (enemy.name, enemy.health))


class Battle:
    def __init__(self, u1, u2):
        self.u1 = u1
        self.u2 = u2
        self.result = "Сражения не было"

    def choose_player(self):
        player1 = input("Выберите первого игрока (Виталя/Игорь/Стас): ")
        player2 = input("Выберите второго игрока (Виталя/Игорь/Стас): ")
        self.u1.set_name(player1)
        self.u2.set_name(player2)

    def choose_attack(self):
        attack1 = input("Выберите атаку для первого игрока (рукой/ногой/головой): ")
        attack2 = input("Выберите атаку для второго игрока (рукой/ногой/головой): ")
        self.u1.change_attack_type(attack1)
        self.u2.change_attack_type(attack2)

    def battle(self):
        while self.u1.health > 0 and self.u2.health > 0:
            n = randint(1, 2)
            if n == 1:
                self.u1.make_kick(self.u2)
            elif n == 2:
                self.u2.make_kick(self.u1)
            else:
                self.u1.make_hit(self.u2)
                self.u2.make_hit(self.u1)
        if self.u1.health > self.u2.health:
            self.result = self.u1.name + " ПОБЕДИЛ"
        elif self.u2.health > self.u1.health:
            self.result = self.u2.name + " ПОБЕДИЛ"

    def who_win(self):
        print(self.result)


# Создаем игроков
first = Soldier('Виталя', 140)
second = Soldier('Хасбик', 100)

# Выбираем игроков и атаки
battle = Battle(first, second)
battle.choose_player()
battle.choose_attack()

# Бой
battle.battle()

battle.who_win()