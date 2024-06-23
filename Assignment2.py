# My name is Yumingqi
# My student ID is 2118040233

import random

class Field:
    def __init__(self, name):
        self.name = name
        self.type = self.change_field()

    def change_field(self):
        fields = ["Toxic Wasteland", "Healing Meadows", "Castle Walls"]
        return random.choice(fields)

class Arena:
    def __init__(self, name):
        self.name = name
        self.field = Field(name)
        self.combatants = []

    def add_combatant(self, combatant):
        if combatant not in self.combatants:
            self.combatants.append(combatant)

    def remove_combatant(self, combatant):
        if combatant in self.combatants:
            self.combatants.remove(combatant)

    def list_combatants(self):
        for combatant in self.combatants:
            print(combatant.details())

    def restore_combatants(self):
        for combatant in self.combatants:
            combatant.reset()

    def duel(self, combatant1, combatant2):
        if combatant1 not in self.combatants or combatant2 not in self.combatants:
            print("Both combatants must be in the arena")
            return
        if combatant1.health <= 0 or combatant2.health <= 0:
            print("Both combatants must have health")
            return

        rounds = 0
        while combatant1.health > 0 and combatant2.health > 0 and rounds < 10:
            self.field_effects(combatant1, combatant2)
            combatant1.attack(combatant2)
            combatant2.attack(combatant1)
            rounds += 1

        print(f"After {rounds} rounds, the duel ended.")
        self.list_combatants()

    def field_effects(self, combatant1, combatant2):
        if self.field.type == "Toxic Wasteland":
            combatant1.take_damage(5)
            combatant2.take_damage(5)
        elif self.field.type == "Healing Meadows":
            combatant1.heal(5)
            combatant2.heal(5)
        # Castle Walls has no effect

class Combatant:
    def __init__(self, name, max_health, strength, defense):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.strength = strength
        self.defense = defense

    def attack(self, opponent):
        damage = self.strength - opponent.defense
        if damage > 0:
            opponent.take_damage(damage)
        else:
            print(f"{self.name} couldn't damage {opponent.name}")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has been defeated!")

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def reset(self):
        self.health = self.max_health

    def details(self):
        return f"{self.name}: Health={self.health}, Strength={self.strength}, Defense={self.defense}"

class Ranger(Combatant):
    def __init__(self, name, max_health, strength, defense, range_level):
        super().__init__(name, max_health, strength, defense)
        self.range_level = range_level
        self.arrows = 3

    def attack(self, opponent):
        if self.arrows > 0:
            damage = self.range_level
            self.arrows -= 1
            print(f"{self.name} fires an arrow at {opponent.name}")
        else:
            damage = self.strength
            print(f"{self.name} attacks {opponent.name} with melee")

        damage -= opponent.defense
        if damage > 0:
            opponent.take_damage(damage)
        else:
            print(f"{self.name} couldn't damage {opponent.name}")

    def reset(self):
        super().reset()
        self.arrows = 3

class Warrior(Combatant):
    def __init__(self, name, max_health, strength, defense, armor_value):
        super().__init__(name, max_health, strength, defense)
        self.armor_value = armor_value

    def take_damage(self, damage):
        reduced_damage = damage - self.armor_value
        if reduced_damage > 0:
            super().take_damage(reduced_damage)
            self.armor_value -= 5
            if self.armor_value < 0:
                self.armor_value = 0
                print(f"{self.name}'s armor has shattered!")
        else:
            print(f"{self.name}'s armor absorbed the damage!")

    def reset(self):
        super().reset()
        self.armor_value = 10

class Mage(Combatant):
    def __init__(self, name, max_health, strength, defense, magic_level):
        super().__init__(name, max_health, strength, defense)
        self.magic_level = magic_level

    def attack(self, opponent):
        raise NotImplementedError("Mages must be specialized!")

class PyroMage(Mage):
    def __init__(self, name, max_health, strength, defense, magic_level):
        super().__init__(name, max_health, strength, defense, magic_level)
        self.flame_boost = 1
        self.mana = magic_level
        self.regen_rate = magic_level // 4

    def attack(self, opponent):
        if self.mana >= 40:
            self.mana -= 40
            self.flame_boost += 1
            print(f"{self.name} casts SuperHeat")
        elif self.mana >= 10:
            self.mana -= 10
            print(f"{self.name} casts FireBlast")

        self.mana += self.regen_rate
        damage = (self.strength * self.flame_boost) + 10 - opponent.defense
        if damage > 0:
            opponent.take_damage(damage)
        else:
            print(f"{self.name} couldn't damage {opponent.name}")

    def reset(self):
        super().reset()
        self.mana = self.magic_level

class FrostMage(Mage):
    def __init__(self, name, max_health, strength, defense, magic_level):
        super().__init__(name, max_health, strength, defense, magic_level)
        self.ice_block = False
        self.mana = magic_level
        self.regen_rate = magic_level // 4
