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

