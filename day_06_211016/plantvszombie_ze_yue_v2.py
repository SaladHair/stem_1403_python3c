"""
Project: PvZ
version: 2.0
author: Ze Yue
"""
"""
[Homework]
Date: 2021-10-16
Refine your class diagram, and write code for your design.
You may add instance attributes and methods to your classes.
"""


class LivingBeing:
    def __init__(self, max_health, health, x, y):
        self.MaxHealth = max_health
        self.Health = health
        self.X = x
        self.Y = y

    def destroy(self):
        pass


class Plant(LivingBeing):
    def __init__(self, cost, max_health, health, x, y):
        super().__init__(max_health, health, x, y)
        self.Cost = cost

    def place(self, x, y):
        pass


class Sunflower(Plant):
    def __init__(self, cost, max_health, health, x, y, generation_speed, generation_amount):
        super().__init__(cost, max_health, health, x, y)
        self.GenerationSpeed = generation_speed
        self.GenerationAmount = generation_amount

    def generate_suns(self, amount):
        pass


class Pea:
    def __init__(self, damage, projectile_speed, fired_by):
        self.Damage = damage
        self.ProjectileSpeed = projectile_speed
        self.FiredBy = fired_by

    def move(self):
        pass

    def on_hit(self, enemy_hit):
        pass


class FrozenPea(Pea):
    def __init__(self, damage, projectile_speed, fired_by):
        super().__init__(damage, projectile_speed, fired_by)

    def slow_enemy(self):
        pass


class Peashooter(Plant):
    def __init__(self, cost, max_health, health, x, y, reload_speed, pea_type):
        super().__init__(cost, max_health, health, x, y)
        self.ReloadSpeed = reload_speed
        self.PeaType = pea_type

    def fire(self, pea, location):
        pass


class SnowPea(Peashooter):
    def __init__(self, cost, max_health, health, x, y, reload_speed, pea_type, slow_duration, slow_percentage):
        super().__init__(cost, max_health, health, x, y, reload_speed, pea_type)
        self.SlowDuration = slow_duration
        self.SlowPercentage = slow_percentage


class WallNut(Plant):
    def __init__(self, cost, max_health, health, x, y):
        super().__init__(cost, max_health, health, x, y)


class PotatoMine(Plant):
    def __init__(self, cost, max_health, health, x, y, explosion_damage):
        super().__init__(cost, max_health, health, x, y)
        self.ExplosionDamage = explosion_damage

    def explode(self):
        pass


class Zombie(LivingBeing):
    def __init__(self, max_health, health, x, y, movement_speed, atk_dmg, atk_spd):
        super().__init__(max_health, health, x, y)
        self.MovementSpeed = movement_speed
        self.AtkDmg = atk_dmg
        self.AtkSpd = atk_spd

    def spawn(self):
        pass

    def walk(self):
        pass


class RegularZombie(Zombie):
    def __init__(self, max_health, health, x, y, movement_speed, atk_dmg, atk_spd):
        super().__init__(max_health, health, x, y, movement_speed, atk_dmg, atk_spd)


class FlagZombie(Zombie):
    def __init__(self, max_health, health, x, y, movement_speed, atk_dmg, atk_spd):
        super().__init__(max_health, health, x, y, movement_speed, atk_dmg, atk_spd)


class ConeHeadZombie(Zombie):
    def __init__(self, max_health, health, x, y, movement_speed, atk_dmg, atk_spd):
        super().__init__(max_health, health, x, y, movement_speed, atk_dmg, atk_spd)


class PoleVaultingZombie(Zombie):
    def __init__(self, max_health, health, x, y, movement_speed, atk_dmg, atk_spd, can_jump):
        super().__init__(max_health, health, x, y, movement_speed, atk_dmg, atk_spd)
        self.can_jump = can_jump

    def jump(self):
        self.can_jump = False
