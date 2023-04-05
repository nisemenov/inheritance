import random
import itertools


class Unit:
    global_number = itertools.count()

    def __init__(self, c):
        self.global_number = next(Unit.global_number) + 1
        self.command = c


class Heroes(Unit):
    number_A = itertools.count()
    number_B = itertools.count()

    def __init__(self, c):
        super().__init__(c)
        self.level = 0
        if self.command == 'A':
            self.personal_number = next(Heroes.number_A) + 1
        else:
            self.personal_number = next(Heroes.number_B) + 1
        self.army = []

    def increase_self_level(self, l):
        self.level += l
        print(f'The hero_{self.personal_number}_{self.command} '
              f'has leveled up to {self.level}.')


class Soldiers(Unit):
    number_A = itertools.count()
    number_B = itertools.count()

    def __init__(self, c):
        super().__init__(c)
        self.my_hero = None
        if self.command == 'A':
            self.personal_number = next(Soldiers.number_A) + 1
        else:
            self.personal_number = next(Soldiers.number_B) + 1

    def go_to_hero(self, hero):
        self.my_hero = f'The hero_{hero.personal_number}_{hero.command}'
        print(f'\nThe soldier_{self.personal_number}_{self.command} '
              f'go to the hero_{hero.personal_number}_{hero.command}.'
              f' Global number of units: {self.global_number} '
              f'and {hero.global_number}.\n')


hero_1_a = Heroes('A')
hero_1_b = Heroes('B')

for i in range(20):
    if random.randint(1, 2) == 1:
        hero_1_a.army.append(Soldiers('A'))
    else:
        hero_1_b.army.append(Soldiers('B'))

print(f'\nQuantity soldiers of command A: {len(hero_1_a.army)}.'
      f'\nQuantity soldiers of command B: {len(hero_1_b.army)}.\n')

if len(hero_1_a.army) >= len(hero_1_b.army):
    hero_1_a.increase_self_level(1)
else:
    hero_1_b.increase_self_level(1)

hero_1_a.army[random.randrange(0, len(hero_1_a.army))].go_to_hero(hero_1_a)
