from unittest import TestCase
from main_logic.day1 import ElfCalories


class TestElfCalories(TestCase):
    def test_max_calories(self):
        data = """1000
        2000
        3000
        
        4000
        
        5000
        6000
        
        7000
        8000
        9000
        
        10000
        """
        actual = ElfCalories.max_calories(self, data)
        self.assertEqual(actual, 24000)

    def test_top_three_sum_of_calories(self):
        data = """1000
        2000
        3000
        
        4000
        
        5000
        6000
        
        7000
        8000
        9000
        
        10000
        """
        actual = ElfCalories.top_three_sum_of_calories(self, data)
        self.assertEqual(actual, 45000)
