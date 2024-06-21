# My name is Yumingqi
# the Student Id is 2118040233
import unittest
from Assignment2 import Field
from Assignment2 import Arena   
from Assignment2 import Combatant  
from Assignment2  import Ranger
from Assignment2 import Warrior

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

  
class TestCombatant(unittest.TestCase):  
  
    def setUp(self):  
        # 在每个测试方法之前都会调用setUp方法，用于设置测试环境  
        self.player = Combatant("Player", 100, 20, 10)  
        self.enemy = Combatant("Enemy", 80, 15, 15)  
  
    def test_attack(self):  
        # 测试攻击时，伤害计算是否正确  
        self.player.attack(self.enemy)  
        expected_damage = 20 - 15  # 玩家力量 - 敌人防御  
        self.assertEqual(self.enemy.health, 80 - expected_damage)  
  
        # 测试攻击时，如果伤害小于等于0，则不造成伤害  
        weak_enemy = Combatant("Weak Enemy", 50, 5, 20)  
        self.player.attack(weak_enemy)  
        self.assertEqual(weak_enemy.health, 50)  
  
    def test_take_damage(self):  
        # 测试受到伤害时，生命值减少是否正确  
        self.enemy.take_damage(20)  
        self.assertEqual(self.enemy.health, 60)  
  
        # 测试当生命值减少到0或以下时，是否变为0并打印消息  
        self.enemy.take_damage(60)  
        self.assertEqual(self.enemy.health, 0)  
  
    def test_heal(self):  
        # 测试治疗时，生命值增加是否正确  
        self.enemy.health = 10  
        self.enemy.heal(30)  
        self.assertEqual(self.enemy.health, 40)  
  
        # 测试当治疗超过最大生命值时，生命值是否变为最大生命值  
        self.enemy.heal(100)  
        self.assertEqual(self.enemy.health, 80)  
  
    def test_reset(self):  
        # 测试重置时，生命值是否恢复为最大生命值  
        self.enemy.health = 20  
        self.enemy.reset()  
        self.assertEqual(self.enemy.health, 80)  
  
    def test_details(self):  
        # 测试details方法是否返回正确的字符串  
        details = self.player.details()  
        self.assertEqual(details, "Player: Health=100, Strength=20, Defense=10") 

class TestRanger(unittest.TestCase):
    def setUp(self):  
        # 在每个测试方法之前设置初始状态  
        self.ranger = Ranger("Ranger1", 100, 10, 5, 20)  
        self.opponent = Combatant("Opponent1", 50, 5, 10)  
  
    def test_attack_with_arrow(self):  
        # 测试使用箭攻击  
        self.ranger.attack(self.opponent)  
        self.assertEqual(self.ranger.arrows, 2)  # 检查箭的数量是否减少  
        self.assertEqual(self.opponent.health, 40)  # 假设对手减少了20点伤害（20 - 10）  
  
    def test_attack_with_melee(self):  
        # 耗尽箭，测试近战攻击  
        self.ranger.arrows = 0  
        self.ranger.attack(self.opponent)  
        self.assertEqual(self.opponent.health, 45)  # 假设对手减少了5点伤害（50 - 5）  
  
    def test_attack_does_not_damage(self):  
        # 测试攻击无法造成伤害的情况  
        opponent_with_high_defense = Combatant("Opponent2", 50, 5, 20)  
        self.ranger.attack(opponent_with_high_defense)  
        self.assertEqual(opponent_with_high_defense.health, 50)  # 没有伤害，因为防御太高  
  
    def test_reset(self):  
        # 测试重置方法  
        self.ranger.attack(self.opponent)  # 先进行一次攻击以改变状态  
        self.ranger.reset()  
        self.assertEqual(self.ranger.arrows, 3)  # 检查箭的数量是否重置  
        # 假设Combatant的reset方法会重置health到max_health，但

  
if __name__ == '__main__':  
    unittest.main()