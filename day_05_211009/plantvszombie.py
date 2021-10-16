"""
Project: PvZ
version: 0.1
author: Ze Yue
"""
"""
[Homework]
Date: 2021-10-09
Due date: 2021-10-15
1. Design a game system in OO
Polish your design
double check and refine classes you found
Write a code framework for the game system you have.
Coding strictly according to your design (namely class diagram)
Submit your code along with your UPDATED class diagram (system design)
Hints:
At least 4 types of plant
At least 4 types of zombie
Search on the Internet for plant and zombie names
"""


class LivingBeing:
    MaxHealth = 0
    Health = 0
    X = 0
    Y = 0

    def destroy(self):
        pass


class Plant(LivingBeing):
    Cost = 0

    def place(self, x, y):
        pass


class Sunflower(Plant):
    Cost = 50
    GenerationSpeed = "fast"
    GenerationAmount = 1

    def generate_suns(self, amount):
        pass


class Pea:
    Damage = 1
    ProjectileSpeed = 1
    FiredBy = 0

    def move(self):
        pass

    def on_hit(self, enemy_hit):
        pass


class FrozenPea(Pea):
    def slow_enemy(self):
        pass


class Peashooter(Plant):
    Cost = 100
    ReloadSpeed = 1
    PeaType = 0

    def fire(self, pea, location):
        pass


class SnowPea(Peashooter):
    Cost = 175
    SlowDuration = 1
    SlowPercentage = 50
    PeaType = FrozenPea


class WallNut(Plant):
    Cost = 50


class PotatoMine(Plant):
    Cost = 25
    ExplosionDamage = 100

    def explode(self):
        pass


class Zombie(LivingBeing):
    MovementSpeed = 0
    AtkDmg = 1
    AtkSpd = 1

    def spawn(self):
        pass

    def walk(self):
        pass


class RegularZombie(Zombie):
    MaxHealth = 270
    MovementSpeed = 1


class FlagZombie(Zombie):
    MaxHealth = 270
    MovementSpeed = 2


class ConeHeadZombie(Zombie):
    MaxHealth = 640
    MovementSpeed = 1


class PoleVaultingZombie(Zombie):
    MaxHealth = 500
    MovementSpeed = 1
    can_jump = True

    def jump(self):
        self.can_jump = False
