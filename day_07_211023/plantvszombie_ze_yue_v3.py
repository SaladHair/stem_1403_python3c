"""
Project: PvZ
version: 3.0
author: Ze Yue
[Homework]
Date: 2021-10-23
Due date: 2021-10-29
1. Write code for your game system in OO
Create at least 3 instances (objects) of plant
Create at least 3 instances (objects) of zombie
Note that more than one type for both plant and zombie instances are supposed to be created.
Describe the battle process between a peashooter and a zombie and write down as a comment
Write some trial code to implement that process in sequence.
Hints:
Coding strictly according to your design (the description of battle process)
Submit your code including your description of the battle process
"""


import time


class Player:
    def __init__(self, suns):
        self.suns = suns


class Grid:
    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.grid = []
        for a in range(self.length*self.height):
            self.grid.append(0)


class LivingBeing:
    def __init__(self, max_health, health, x, y, grid, class_name):
        self.grid = grid
        self.class_name = class_name
        self.max_health = max_health
        self.health = health
        self.x = x
        self.y = y
        grid.grid[y*grid.length+x] = self

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.class_name} took {amount} damage")
        if self.health <= 0:
            print(f"{self.class_name} died")
            self.grid.grid[self.y * self.grid.length + self.x] = 0
            if self in plants:
                plants.remove(self)
            if self in peashooters:
                peashooters.remove(self)
            if self in sunflowers:
                sunflowers.remove(self)
            if self in zombies:
                zombies.remove(self)
            if self in pole_vaulting_zombies:
                pole_vaulting_zombies.remove(self)

            del self


class Plant(LivingBeing):
    def __init__(self, cost, max_health, health, x, y, grid, class_name, player):
        super().__init__(max_health, health, x, y, grid, class_name)
        self.cost = cost
        player.suns -= self.cost


def generate_suns(amount):
    player_object.suns += amount


class Sunflower(Plant):
    def __init__(self, cost, max_health, health, x, y, generation_speed, generation_amount, grid, class_name, player):
        super().__init__(cost, max_health, health, x, y, grid, class_name, player)
        self.generation_speed = generation_speed
        self.generation_amount = generation_amount


class Pea:
    def __init__(self, damage, projectile_speed, fired_by, x, y, grid):
        self.damage = damage
        self.projectile_speed = projectile_speed
        self.fired_by = fired_by
        self.x = x
        self.y = y
        self.grid = grid

    def move(self):
        if self.grid.grid[self.y*self.grid.length+self.x] in zombies:
            print(f"{self.fired_by.class_name} attacked {self.grid.grid[self.y * self.grid.length + self.x].class_name}, dealing {self.damage} damage")
            self.grid.grid[self.y * self.grid.length + self.x].take_damage(self.damage)
            del self
        else:
            self.x += self.projectile_speed
            print(f"Pea moved to ({self.x}, {self.y})")
            if self.grid.grid[self.y*self.grid.length+self.x] in zombies:
                print(f"{self.fired_by.class_name} attacked {self.grid.grid[self.y * self.grid.length + self.x].class_name}, dealing {self.damage} damage")
                self.grid.grid[self.y * self.grid.length + self.x].take_damage(self.damage)
                del self


class FrozenPea(Pea):
    def __init__(self, damage, projectile_speed, fired_by, x, y, grid):
        super().__init__(damage, projectile_speed, fired_by, x, y, grid)

    def slow_enemy(self):
        pass


class Peashooter(Plant):
    def __init__(self, cost, max_health, health, x, y, reload_speed, pea_type, grid, class_name, player):
        super().__init__(cost, max_health, health, x, y, grid, class_name, player)
        self.grid = grid
        self.player = player
        self.reload_speed = reload_speed
        self.pea_type = pea_type

    def fire(self):
        if self.pea_type == "Pea":
            peas.append(Pea(50, 1, self, self.x, self.y, self.grid))
            print(f"Pea spawned at ({self.x}, {self.y})")
        elif self.pea_type == "FrozenPea":
            peas.append(FrozenPea(50, 1, self, self.x, self.y, self.grid))
            print(f"FrozenPea spawned at ({self.x}, {self.y})")


class SnowPea(Peashooter):
    def __init__(self, cost, max_health, health, x, y, reload_speed, pea_type, slow_duration, slow_percentage, grid, class_name, player):
        super().__init__(cost, max_health, health, x, y, reload_speed, pea_type, grid, class_name, player)
        self.slow_duration = slow_duration
        self.slow_percentage = slow_percentage


class WallNut(Plant):
    def __init__(self, cost, max_health, health, x, y, grid, class_name, player):
        super().__init__(cost, max_health, health, x, y, grid, class_name, player)


class PotatoMine(Plant):
    def __init__(self, cost, max_health, health, x, y, explosion_damage, grid, class_name, player):
        super().__init__(cost, max_health, health, x, y, grid, class_name, player)
        self.explosion_damage = explosion_damage

    def explode(self):
        pass


class Zombie(LivingBeing):

    def __init__(self, max_health, health, x, y, movement_speed, atk_dmg, atk_spd, grid, class_name):
        super().__init__(max_health, health, x, y, grid, class_name)
        self.class_name = class_name
        self.grid = grid
        self.movement_speed = movement_speed
        self.atk_dmg = atk_dmg
        self.atk_spd = atk_spd

    def walk(self):
        global game
        print(f"{self.class_name} walked to {self.x}, {self.y}")
        if self.grid.grid[self.y*self.grid.length+self.x-self.movement_speed] in plants:
            print(f"{self.class_name} attacked {self.grid.grid[self.y*self.grid.length+self.x-self.movement_speed].class_name}, dealing {self.atk_dmg} damage")
            self.grid.grid[self.y * self.grid.length + self.x - self.movement_speed].take_damage(self.atk_dmg)
        else:
            self.grid.grid[self.y*self.grid.length+self.x] = 0
            self.x -= self.movement_speed
            self.grid.grid[self.y * self.grid.length + self.x] = self
        if self.x <= 0:
            print("zombies won the game")
            game = "finished"


class RegularZombie(Zombie):
    def __init__(self, max_health, health, x, y, movement_speed, atk_dmg, atk_spd, grid, class_name):
        super().__init__(max_health, health, x, y, movement_speed, atk_dmg, atk_spd, grid, class_name)


class PoleVaultingZombie(Zombie):
    def __init__(self, max_health, health, x, y, movement_speed, atk_dmg, atk_spd, can_jump, grid, class_name):
        super().__init__(max_health, health, x, y, movement_speed, atk_dmg, atk_spd, grid, class_name)
        self.can_jump = can_jump

    def jump(self):
        self.can_jump = False


grid_object = Grid(10, 10)
player_object = Player(500)

plants = []
sunflowers = []
peashooters = []
pole_vaulting_zombies = []
zombies = []
peas = []

peashooter1 = Peashooter(50, 500, 500, 3, 2, 1, "Pea", grid_object, "Peashooter1", player_object)
print("Peashooter 1 spawned at (3,2)")
peashooters.append(peashooter1)
plants.append(peashooter1)
zombie1 = Zombie(500, 500, grid_object.length, 2, 1, 50, 1, grid_object, "Zombie1")
print("Zombie 1 spawned at (10, 2)")
zombies.append(zombie1)

game = "playing"

while game == "playing":
    generate_suns(len(sunflowers)*50)  # Sunflowers generate suns
    for i in peas:
        i.move()  # Bullets advance toward Zombies, deal dmg if hit
    for i in peashooters:
        i.fire()  # Peashooters shoot bullets
    for i in zombies:
        i.walk()  # Zombies walk forward
    if not zombies:
        print("zombies all died, plants win")
        game = "finished"
    time.sleep(1)
