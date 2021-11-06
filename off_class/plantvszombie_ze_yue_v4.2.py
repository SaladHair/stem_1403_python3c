"""
Project: PvZ
version: 4.1
author: Ze Yue
[Homework]
Date: 2021-10-30
Due date: 2021-10-05
1. Write code for your game system in OO
task a. Refactor your code
task b. Add a feature of resources (sunlight) collecting and consuming
Hints:
Design and add a class named Resource
This class enables players to collect the sunlight produced by sunflowers.
It also enables players to consume sunlight for placing plants.
Update your class diagram if necessary.
Submit your code and updated class diagram.
"""


import time


class Resource:
    def __init__(self, sun_amount):
        self.sun_amount = sun_amount

    def generate_suns(self, amount):
        self.sun_amount += amount

    def remove_suns(self, amount):
        self.sun_amount -= amount


class Grid:
    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.grid = []
        for a in range(self.length*self.height):
            self.grid.append(0)


class Player:
    def __init__(self, resource, grid):
        self.resource = resource
        self.grid = grid


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

class Plant(LivingBeing):
    def __init__(self, cost, max_health, health, x, y, class_name, player):
        super().__init__(max_health, health, x, y, player.grid, class_name)
        self.cost = cost
        if player.resource.sun_amount >= self.cost:
            player.resource.remove_suns(self.cost)
            plants.append(self)
            print(f"{self.class_name} spawned at ({self.x}, {self.y})")
        else:
            print(f"{self.class_name} was unable to spawn at ({self.x}, {self.y}) due to a lack of suns in the player's inventory.")


class Sunflower(Plant):
    def __init__(self, x, y, class_name, player, cost=50, max_health=500, health=500, generation_speed=1, generation_amount=50):
        super().__init__(cost, max_health, health, x, y, class_name, player)
        sunflowers.append(self)
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
        else:
            self.x += self.projectile_speed
            print(f"Pea moved to ({self.x}, {self.y})")
            if self.grid.grid[self.y*self.grid.length+self.x] in zombies:
                print(f"{self.fired_by.class_name} attacked {self.grid.grid[self.y * self.grid.length + self.x].class_name}, dealing {self.damage} damage")
                self.grid.grid[self.y * self.grid.length + self.x].take_damage(self.damage)


class FrozenPea(Pea):
    def __init__(self, damage, projectile_speed, fired_by, x, y, grid):
        super().__init__(damage, projectile_speed, fired_by, x, y, grid)

    def slow_enemy(self):
        pass


class Peashooter(Plant):
    def __init__(self, x, y, class_name, player, cost=50, max_health=500, health=500, reload_speed=1, pea_type="Pea"):
        super().__init__(cost, max_health, health, x, y, class_name, player)
        peashooters.append(self)
        self.grid = player.grid
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
    def __init__(self, cost, max_health, health, x, y, reload_speed, slow_duration, slow_percentage, class_name, player, pea_type="FrozenPea"):
        super().__init__(cost, max_health, health, x, y, reload_speed, class_name, player, pea_type=pea_type)
        self.slow_duration = slow_duration
        self.slow_percentage = slow_percentage


class WallNut(Plant):
    def __init__(self, cost, max_health, health, x, y, class_name, player):
        super().__init__(cost, max_health, health, x, y, class_name, player)


class PotatoMine(Plant):
    def __init__(self, cost, max_health, health, x, y, explosion_damage, class_name, player):
        super().__init__(cost, max_health, health, x, y, class_name, player)
        self.explosion_damage = explosion_damage

    def explode(self):
        pass


class Zombie(LivingBeing):

    def __init__(self, max_health, health, x, y, movement_speed, atk_dmg, atk_spd, grid, class_name):
        super().__init__(max_health, health, x, y, grid, class_name)
        zombies.append(self)
        print(f"{self.class_name} spawned at ({self.x}, {self.y})")
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
resource_object = Resource(500)
player_object = Player(resource_object, grid_object)

plants = []
sunflowers = []
peashooters = []
pole_vaulting_zombies = []
zombies = []
peas = []

peashooter1 = Peashooter(3, 2, "Peashooter1", player_object)

peashooter2 = Peashooter(3, 4, "Peashooter2", player_object)

peashooter3 = Peashooter(2, 4, "Peashooter3", player_object)

sunflower1 = Sunflower(3, 7, "Sunflower1", player_object)

zombie1 = Zombie(270, 270, grid_object.length, 2, 1, 50, 1, grid_object, "Zombie1")

zombie2 = Zombie(270, 270, grid_object.length-1, 4, 1, 50, 1, grid_object, "Zombie2")

# Cone zombie but since it doesnt have additional functions, I used the basic zombie class to spawn it
cone_zombie1 = Zombie(750, 750, grid_object.length, 4, 1, 50, 1, grid_object, "ConeZombie1")

game = "playing"

while game == "playing":
    resource_object.generate_suns(len(sunflowers)*50)  # Sunflowers generate suns
    print(f"The player has {resource_object.sun_amount} suns")
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
