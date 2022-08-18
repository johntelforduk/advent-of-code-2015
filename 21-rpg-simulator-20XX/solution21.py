# Solution to day 21 of AOC 2015, RPG Simulator 20XX
# https://adventofcode.com/2015/day/21

import itertools


class Player:

    def __init__(self, name: str, gold: int, hit_points: int, damage: int, armor: int):
        self.name = name
        self.gold = gold
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor
        self.loser = False

    def print(self):
        print('name, gold, hit_points, damage, armor: ',
              self.name, self.gold, self.hit_points, self.damage, self.armor)


def turn(attacker: Player, defender: Player):
    # "Each attack reduces the opponent's hit points by at least 1."
    # "Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score."
    this_damage = max(1, attacker.damage - defender.armor)
    defender.hit_points -= this_damage
    if defender.hit_points <= 0:
        defender.loser = True


def game(p1, p2):
    attacker = 'p1'
    while p1.loser is False and p2.loser is False:
        if attacker == 'p1':
            turn(attacker=p1, defender=p2)
            # p2.print()
            attacker = 'p2'
        else:
            turn(attacker=p2, defender=p1)
            # p1.print()
            attacker = 'p1'


weaponry = [(8, 4, 0),
            (10, 5, 0),
            (25, 6, 0),
            (40, 7, 0),
            (74, 8, 0)]

armory = [(0, 0, 0),                # "Armor is optional..."
          (13, 0, 1),
          (31, 0, 2),
          (53, 0, 3),
          (75, 0, 4),
          (102, 0, 5)]

rings = [(0, 0, 0),                 # "You can buy 0-2 rings..."
         (0, 0, 0),
         (25, 1, 0),
         (50, 2, 0),
         (100, 3, 0),
         (20, 0, 1),
         (40, 0, 2),
         (80, 0, 3)]

# Example given in puzzle.
player1 = Player(name='player1', gold=0, hit_points=8, damage=5, armor=5)
boss = Player(name='boss', gold=0, hit_points=12, damage=7, armor=2)
game(player1, boss)
print(boss.loser)


cheapest_winner = None
# Make each possible load out of player1.
for wg, wd, wa in weaponry:
    for ag, ad, aa in armory:
        for ((r1g, r1d, r1a), (r2g, r2d, r2a)) in list(itertools.permutations(rings, 2)):
            g = wg + ag + r1g + r2g
            d = wd + ad + r1d + r2d
            a = wa + aa + r1a + r2a

            player1 = Player(name='player1', gold=g, hit_points=100, damage=d, armor=a)
            # player1.print()
            boss = Player(name='boss', gold=0, hit_points=103, damage=9, armor=2)

            game(p1=player1, p2=boss)
            if boss.loser and (cheapest_winner is None or player1.gold < cheapest_winner):
                cheapest_winner = player1.gold
                print(cheapest_winner)
