# My name is Yumingqi
# the Student Id is 2118040233


import unittest
from Assignment2 import Field 
from Assignment2 import Arena   
from Assignment2 import Combatant  
from Assignment2  import Ranger
from Assignment2 import Warrior
from Assignment2 import Mage
from Assignment2 import PyroMage
from Assignment2 import FrostMage
from Assignment2 import Dharok
from Assignment2 import Guthans
from Assignment2 import Karil

import io  
import contextlib  

class TestField(unittest.TestCase):  
    def setUp(self):  
        self.field = Field('Test Field')  
  
    def test_change_field_returns_valid_type(self):    
        fields = ["Toxic Wasteland", "Healing Meadows", "Castle Walls"]  
        self.assertIn(self.field.type, fields)  
  
    def test_init_sets_type_correctly(self):    
        self.assertIsNotNone(self.field.type)  
 
 
class TestArena(unittest.TestCase):  
  
    def setUp(self):  
        self.arena = Arena("Test Arena")  
        self.combatant1 = Combatant("Combatant 1")  
        self.combatant2 = Combatant("Combatant 2")  
        self.arena.addCombatant(self.combatant1)  
        self.arena.addCombatant(self.combatant2)  
  
    def test_add_combatant(self):  
        self.assertIn(self.combatant1, self.arena.combatants)  
        self.assertIn(self.combatant2, self.arena.combatants)  
  
    def test_remove_combatant(self):  
        self.arena.removeCombatant(self.combatant1)  
        self.assertNotIn(self.combatant1, self.arena.combatants)  
        self.assertIn(self.combatant2, self.arena.combatants)  
  
    def test_duel_with_both_alive(self):    
        self.combatant1.health = 100  
        self.combatant2.health = 100  
        self.arena.field = Field("Empty Field")    
        self.arena.duel(self.combatant1, self.combatant2)  
        self.assertTrue(self.combatant1.health < 100 or self.combatant2.health < 100)  
  
    def test_duel_with_toxic_wasteland(self):  
        self.combatant1.health = 20  
        self.combatant2.health = 20  
        self.arena.field = Field("Toxic Wasteland")  
        self.arena.duel(self.combatant1, self.combatant2)    
        self.assertEqual(self.combatant1.health, 0)  
        self.assertEqual(self.combatant2.health, 0)  
  
    def test_duel_with_healing_meadows(self):  
        self.combatant1.health = 10  
        self.combatant2.health = 10  
        self.arena.field = Field("Healing Meadows")   
        self.arena.duel(self.combatant1, self.combatant2)  
        self.assertTrue(self.combatant1.health > 0)  
        self.assertTrue(self.combatant2.health > 0)  
  
class TestCombatant(unittest.TestCase):  
  
    def setUp(self):    
        self.player = Combatant("Player", 100, 20, 10)  
        self.enemy = Combatant("Enemy", 80, 15, 15)  
  
    def test_attack(self):    
        self.player.attack(self.enemy)  
        expected_damage = 20 - 15  
        self.assertEqual(self.enemy.health, 80 - expected_damage)  
        weak_enemy = Combatant("Weak Enemy", 50, 5, 20)  
        self.player.attack(weak_enemy)  
        self.assertEqual(weak_enemy.health, 50)  
  
    def test_take_damage(self):   
        self.enemy.take_damage(20)  
        self.assertEqual(self.enemy.health, 60)  
        self.enemy.take_damage(60)  
        self.assertEqual(self.enemy.health, 0)  
  
    def test_heal(self):
        self.enemy.health = 10  
        self.enemy.heal(30)  
        self.assertEqual(self.enemy.health, 40)  
        self.enemy.heal(100)  
        self.assertEqual(self.enemy.health, 80)  
  
    def test_reset(self):  
        self.enemy.health = 20  
        self.enemy.reset()  
        self.assertEqual(self.enemy.health, 80)  
  
    def test_details(self):   
        details = self.player.details()  
        self.assertEqual(details, "Player: Health=100, Strength=20, Defense=10") 

class TestRanger(unittest.TestCase):
    def setUp(self):  
        self.ranger = Ranger("Ranger1", 100, 10, 5, 20)  
        self.opponent = Combatant("Opponent1", 50, 5, 10)  
  
    def test_attack_with_arrow(self):  
        self.ranger.attack(self.opponent)  
        self.assertEqual(self.ranger.arrows, 2)    
        self.assertEqual(self.opponent.health, 40)    
  
    def test_attack_with_melee(self):  
        self.ranger.arrows = 0  
        self.ranger.attack(self.opponent)  
        self.assertEqual(self.opponent.health, 45)    
  
    def test_attack_does_not_damage(self):    
        opponent_with_high_defense = Combatant("Opponent2", 50, 5, 20)  
        self.ranger.attack(opponent_with_high_defense)  
        self.assertEqual(opponent_with_high_defense.health, 50)   
  
    def test_reset(self):    
        self.ranger.attack(self.opponent)    
        self.ranger.reset()  
        self.assertEqual(self.ranger.arrows, 3)  

class TestWarrior(unittest.TestCase):
    def setUp(self):
        self.warrior= Warrior("Test Warrior", 100, 10, 5, 10)  
    def test_take_damage_with_armor(self):
        self.warrior.take_damage(5)
        self.assertEqual(self.warrior.health, 100)
        self.assertEqual(self.warrior.armor_value,5)
    def test_take_damage_without_armor(self):
        self.warrior.armor_value = 0  
        self.warrior.take_damage(5) 
        self.assertEqual(self.warrior.health, 95)
    def test_take_damage_shatters_armor(self):  
        self.warrior.take_damage(15)  
        self.assertEqual(self.warrior.armor_value, 0)  
        self.assertTrue("Test Warrior's armor has shattered!" in self.output.getvalue()) 
    def test_reset(self):
        self.warrior.take_damage(20) 
        self.warrior.reset()
        self.assertEqual(self.warrior.health, 100)
        self.assertEqual(self.warrior.armor_value, 5)

class TestMage(unittest.TestCase):
    def setUp(self):
        self.mage=Mage("Test Mage",100,5,20,15)

    def tset_attack(self):
        self.assertEqual(self.mage.max_health,100)
        self.assertEqual(self.mage.strength,5)

    def test_mage_attack_raises_not_implemented_error(self):  
        mage = Mage('Merlin', 100, 5, 10, 20) 
        class MockCombatant:  
            pass  
        opponent = MockCombatant()
        with self.assertRaises(NotImplementedError) as context:  
            mage.attack(opponent)  
        self.assertEqual(str(context.exception), "Mages must be specialized!")  

class TestPyroMage(unittest.TestCase):
    def setUp(self):
        self.pyroMage = PyroMage("PyroMage",100,20,5,80)
        self.opponent = Mage("Enemy", 100, 15, 10, 0)
        self.pyromage.attack(self.opponent)  
    def test_attack_with_sufficient_mana_for_superheat(self):
        self.assertEqual(self.pyromage.mana, 40)  
        self.assertEqual(self.pyromage.flame_boost, 2)    
        self.assertLess(self.opponent.health, 100) 
    
    def test_attack_with_sufficient_mana_for_fireblast(self):
        self.pyromage.mana = 15  
        self.pyromage.attack(self.opponent)  
        self.assertEqual(self.pyromage.mana, 5) 
        self.assertEqual(self.pyromage.flame_boost, 1)  
        self.assertLess(self.opponent.health, 100) 

    def test_attack_with_insufficient_mana(self):
        self.pyromage.mana = 5  
        self.pyromage.attack(self.opponent)  
        self.assertEqual(self.pyromage.mana, 9)   
        self.assertEqual(self.pyromage.flame_boost, 1)  
        self.assertEqual(self.opponent.health, 100)  
    
    def test_reset(self):
        self.assertEqual(self.pyroMage.health,self.pyroMage.max_health)
        self.assertEqual(self.pyromage.mana, 80)

class TestFrostMage(unittest.TestCase):
    
    def setUp(self):
        self.mage = FrostMage("Icicle", max_health=100, strength=10, defense=5, magic_level=50)
    
    def test_attack_with_enough_mana(self):
        opponent = Mage("Enemy", max_health=100, strength=10, defense=5, magic_level=50)
        self.mage.mana = 50
        self.mage.attack(opponent)
        self.assertTrue(self.mage.ice_block)
        self.assertEqual(self.mage.mana, 0)  
        
    def test_attack_with_insufficient_mana(self):
        opponent = Mage("Enemy", max_health=100, strength=10, defense=5, magic_level=50)
        self.mage.mana = 9
        self.mage.attack(opponent)
        self.assertFalse(self.mage.ice_block)
        self.assertEqual(self.mage.mana, 12)  
        
    def test_attack_with_ice_block_active(self):
        opponent = Mage("Enemy", max_health=100, strength=10, defense=5, magic_level=50)
        self.mage.ice_block = True
        self.mage.attack(opponent)
        self.assertTrue(self.mage.ice_block)
        self.assertEqual(self.mage.mana, 12)  
    
    def test_reset_method(self):
        self.mage.mana = 30
        self.mage.ice_block = True
        self.mage.reset()
        self.assertEqual(self.mage.mana, 50)  
        self.assertFalse(self.mage.ice_block)

class TestDharok(unittest.TestCase):  
    def setUp(self):    
        self.dharok = Dharok("Dharok", 100, 20, 5)  
        self.opponent = Warrior("Enemy", 100, 15, 10)  
  
    def test_attack_with_positive_damage(self):   
        self.dharok.attack(self.opponent)  
        expected_damage  = 10  
        self.assertEqual(self.opponent.health, 100 - expected_damage)  
  
    def test_attack_with_negative_damage(self):    
        self.dharok.health = 50  
        with self.assertLogs(level='INFO') as cm:  
            self.dharok.attack(self.opponent)  
            self.assertIn(f"Dharok couldn't damage Enemy", cm.output)  
        self.assertEqual(self.opponent.health, 100)  
  
    def test_attack_with_zero_damage(self):  
        self.dharok.health = 90  
        self.opponent.defense = 15  
        with self.assertLogs(level='INFO') as cm:  
            self.dharok.attack(self.opponent)  
            self.assertIn(f"Dharok couldn't damage Enemy", cm.output)  
        self.assertEqual(self.opponent.health, 100)

class TestGuthans(unittest.TestCase):  
    def setUp(self):    
        self.guthans = Guthans("Guthans", 50)  
        self.opponent = Warrior("Enemy", 30)  
        self.opponent.defense = 20   
  
    def test_attack_and_heal(self):  
        initial_guthans_health = self.guthans.health  
        initial_opponent_health = self.opponent.health  

        self.guthans.attack(self.opponent)   
        self.assertLess(self.opponent.health, initial_opponent_health)  
        self.assertGreater(self.guthans.health, initial_guthans_health)  
  
    def test_attack_no_damage(self):  
        strong_opponent = Warrior("Strong Enemy", 50)  
        strong_opponent.defense = 50  
        initial_guthans_health = self.guthans.health  
        self.guthans.attack(strong_opponent)   
        self.assertEqual(self.guthans.health, initial_guthans_health)       

class TestKaril(unittest.TestCase):  
    def setUp(self):  
        self.karil = Karil("Karil", 100, 50, 10, 5, 15)  
        self.opponent = Warrior("Enemy", 100, 30, 20, 0)  
  
    def test_attack_causes_damage(self):  
        
        initial_opponent_health = self.opponent.health  
        self.karil.attack(self.opponent)  
        self.assertLess(self.opponent.health, initial_opponent_health)  
  
    def test_attack_no_damage(self):
        strong_opponent = Warrior("Strong Enemy", 100, 30, 45, 0)  
        initial_opponent_health = strong_opponent.health  
        captured_output = io.StringIO()   
        with contextlib.redirect_stdout(captured_output):  
            self.karil.attack(strong_opponent)  
  
        self.assertEqual(strong_opponent.health, initial_opponent_health)  
        self.assertIn("couldn't damage", captured_output.getvalue())  
  



if __name__ == '__main__':  
    unittest.main()