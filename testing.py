import unittest
from Assignment2 import Field
from Assignment2 import Arena  # 假设Arena类定义在arena.py文件中  
from Assignment2 import Combatant  # 假设Combatant类定义在combatant.py文件中 

class TestField(unittest.TestCase):  
    def setUp(self):  
        # 在每个测试方法运行前创建Field对象  
        self.field = Field('Test Field')  
  
    def test_change_field_returns_valid_type(self):  
        # 确保self.field.type是fields列表中的一个元素  
        fields = ["Toxic Wasteland", "Healing Meadows", "Castle Walls"]  
        self.assertIn(self.field.type, fields)  
  
    def test_init_sets_type_correctly(self):  
        # 确保__init__设置了self.type  
        self.assertIsNotNone(self.field.type)  
 
 
class TestArena(unittest.TestCase):  
  
    def setUp(self):  
        self.arena = Arena("Test Arena")  
        self.combatant1 = Combatant("Combatant 1")  
        self.combatant2 = Combatant("Combatant 2")  
        self.arena.add_combatant(self.combatant1)  
        self.arena.add_combatant(self.combatant2)  
  
    def test_add_combatant(self):  
        self.assertIn(self.combatant1, self.arena.combatants)  
        self.assertIn(self.combatant2, self.arena.combatants)  
  
    def test_remove_combatant(self):  
        self.arena.remove_combatant(self.combatant1)  
        self.assertNotIn(self.combatant1, self.arena.combatants)  
        self.assertIn(self.combatant2, self.arena.combatants)  
  
    def test_duel_with_both_alive(self):  
        # 这里假设Combatant类有足够的生命值，且攻击和防御逻辑简单  
        # 例如：每次攻击减少对方10点生命值，且自身不受伤害  
        self.combatant1.health = 100  
        self.combatant2.health = 100  
        self.arena.field = Field("Empty Field")  # 假设有一个不产生效果的场地  
        self.arena.duel(self.combatant1, self.combatant2)  
        self.assertTrue(self.combatant1.health < 100 or self.combatant2.health < 100)  
  
    def test_duel_with_toxic_wasteland(self):  
        self.combatant1.health = 20  
        self.combatant2.health = 20  
        self.arena.field = Field("Toxic Wasteland")  
        self.arena.duel(self.combatant1, self.combatant2)  
        # 假设每个回合都会因为场地效果减少5点生命值  
        # 假设每回合战斗也会减少生命值（这里简化为直接减少到0）  
        self.assertEqual(self.combatant1.health, 0)  
        self.assertEqual(self.combatant2.health, 0)  
  
    def test_duel_with_healing_meadows(self):  
        self.combatant1.health = 10  
        self.combatant2.health = 10  
        self.arena.field = Field("Healing Meadows")  
        # 假设在这个场地中，即使每回合有攻击，由于场地效果，生命值不会减少到0  
        # 这里只是检查场地效果是否被应用  
        self.arena.duel(self.combatant1, self.combatant2)  
        self.assertTrue(self.combatant1.health > 0)  
        self.assertTrue(self.combatant2.health > 0)  
  
    # 可能还需要其他测试，例如测试非法战斗（不在竞技场中的战斗者）等  
  
if __name__ == '__main__':  
    unittest.main()