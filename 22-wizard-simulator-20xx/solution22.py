# Solution to day 22 of AOC 2015, Wizard Simulator 20XX
# https://adventofcode.com/2015/day/22

from copy import copy

TEST = True


class Game(object):

    def __init__(self, player_hit_points: int, player_mana: int,
                 boss_hit_points: int, boss_damage: int):
        self.player_hit_points = player_hit_points
        self.player_mana = player_mana
        self.player_mana_spent = 0
        self.player_armor = 0

        self.boss_hit_points = boss_hit_points
        self.boss_damage = boss_damage

        self.shield_timer = 0
        self.poison_timer = 0
        self.recharge_timer = 0

        self.winner = ''                # '' means game in progress, or 'player' or 'boss'
        if TEST:
            print('NEW GAME!')

    def magic_missile(self) -> bool:
        """Magic Missile costs 53 mana. It instantly does 4 damage."""
        self.player_mana -= 53
        if self.player_mana < 0:
            return False
        self.player_mana_spent += 53
        self.boss_hit_points -= 4
        if TEST:
            print('Player casts Magic Missile, dealing 4 damage.')
        return True

    def drain(self) -> bool:
        """Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points."""
        self.player_mana -= 73
        if self.player_mana < 0:
            return False
        self.player_mana_spent += 73
        self.boss_hit_points -= 2
        self.player_hit_points += 2
        if TEST:
            print('Player casts Drain, dealing 2 damage, and healing 2 hit points.')
        return True

    def shield(self) -> bool:
        """Shield costs 113 mana. It starts an effect that lasts for 6 turns.
        While it is active, your armor is increased by 7."""
        self.player_mana -= 113
        if self.player_mana < 0 or self.shield_timer > 0:
            return False
        self.player_mana_spent += 113
        self.shield_timer = 6
        self.player_armor += 7
        if TEST:
            print('Player casts Shield, increasing armor by 7.')
        return True

    def poison(self) -> bool:
        """Poison costs 173 mana. It starts an effect that lasts for 6 turns.
        At the start of each turn while it is active, it deals the boss 3 damage."""
        self.player_mana -= 173
        if self.player_mana <= 0 or self.poison_timer > 0:
            return False
        self.player_mana_spent += 173
        self.poison_timer = 6
        if TEST:
            print('Player casts Poison.')
        return True

    def recharge(self) -> bool:
        """Recharge costs 229 mana. It starts an effect that lasts for 5 turns.
        At the start of each turn while it is active, it gives you 101 new mana."""
        self.player_mana -= 229
        if self.player_mana <= 0 or self.recharge_timer > 0:
            return False
        self.player_mana_spent += 229
        self.recharge_timer = 5
        if TEST:
            print('Player casts Recharge.')
        return True

    def every_turn(self):
        if self.shield_timer > 0:
            self.shield_timer -= 1
            if TEST:
                print(f"Shield's timer is now {self.shield_timer}.")
            if self.shield_timer == 0:
                self.player_armor -= 7
                if TEST:
                    print('Shield wears off, decreasing armor by 7.')

        if self.poison_timer > 0:
            self.poison_timer -= 1
            self.boss_hit_points -= 3
            if TEST:
                print(f'Poison deals 3 damage; its timer is now {self.poison_timer}.')

        if self.recharge_timer > 0:
            self.recharge_timer -= 1
            self.player_mana += 101
            if TEST:
                print(f'Recharge provides 101 mana; its timer is now {self.recharge_timer}.')
            if self.recharge_timer == 0 and TEST:
                print('Recharge wears off.')

        self.check_winner()

    def check_winner(self):
        if len(self.winner) != 0:
            return
        if self.player_hit_points <= 0:
            self.winner = 'boss'
            if TEST:
                print('The boss wins')
        elif self.boss_hit_points <= 0:
            self.winner = 'player'
            if TEST:
                print('The player wins')

    def player_turn(self, attack):
        if TEST:
            print('\n-- Player turn --')
            self.print_player()
            self.print_boss()
        self.every_turn()
        if attack():                # If true, the attack succeeded...
            self.check_winner()     # So check if there is a winner yet.
        else:                       # Attack failed - so boss won.
            self.winner = 'boss'

    def boss_turn(self):
        if TEST:
            print('\n-- Boss turn --')
            self.print_player()
            self.print_boss()
        self.every_turn()
        if self.winner != 'player':
            if self.player_armor == 0:
                self.player_hit_points -= self.boss_damage
                if TEST:
                    print(f'Boss attacks for {self.boss_damage} damage.')
            else:
                this_damage = self.boss_damage - self.player_armor
                self.player_hit_points -= this_damage
                if TEST:
                    print(f'Boss attacks for {self.boss_damage} - {self.player_armor} = {this_damage} damage')
            self.check_winner()

    def print_player(self):
        print(f'- Player has {self.player_hit_points} hit points, {self.player_armor} armor, {self.player_mana} mana')

    def print_boss(self):
        print(f'- Boss has {self.boss_hit_points} hit points')


# First example given in puzzle.
example_game1 = Game(player_hit_points=10, player_mana=250, boss_hit_points=13, boss_damage=8)
example_game1.player_turn(attack=example_game1.poison)
example_game1.boss_turn()
example_game1.player_turn(attack=example_game1.magic_missile)
example_game1.boss_turn()

# Second example given in puzzle.
example_game2 = Game(player_hit_points=10, player_mana=250, boss_hit_points=14, boss_damage=8)
example_game2.player_turn(attack=example_game2.recharge)
example_game2.boss_turn()
example_game2.player_turn(attack=example_game2.shield)
example_game2.boss_turn()
example_game2.player_turn(attack=example_game2.drain)
example_game2.boss_turn()
example_game2.player_turn(attack=example_game2.poison)
example_game2.boss_turn()
example_game2.player_turn(attack=example_game2.magic_missile)
example_game2.boss_turn()


def search_games(this_game: Game, turn: str):
    global CHEAPEST
    if this_game.winner == 'boss':
        return
    if this_game.winner == 'player':
        if CHEAPEST is None or this_game.player_mana_spent < CHEAPEST:
            CHEAPEST = this_game.player_mana_spent
            print(CHEAPEST)
        return

    if turn == 'boss':
        this_game.boss_turn()
        search_games(this_game, turn='player')
    else:
        for each_attack in range(5):
            new_game = copy(this_game)
            possible_attacks = {0: new_game.magic_missile, 1: new_game.drain, 2: new_game.shield,
                                3: new_game.poison, 4: new_game.recharge}
            chosen_attack = possible_attacks[each_attack]
            new_game.player_turn(attack=chosen_attack)
            search_games(new_game, 'boss')


TEST = False
CHEAPEST = None

game = Game(player_hit_points=50, player_mana=500, boss_hit_points=71, boss_damage=10)
search_games(game, 'player')
