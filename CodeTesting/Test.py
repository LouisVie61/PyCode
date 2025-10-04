import unittest
from ChickenAndDog import calculate_chicken_and_dog

class TestChickenDog(unittest.TestCase):
    def test_valid_case(self):
        # 36 con, 100 chân -> 14 chó, 22 gà
        self.assertEqual(calculate_chicken_and_dog(36, 100), [14, 22])

    def test_m_odd(self):
        # m lẻ -> invalid
        self.assertEqual(calculate_chicken_and_dog(10, 25), [])

    def test_m_out_of_range(self):
        # m nhỏ hơn 2n -> invalid
        self.assertEqual(calculate_chicken_and_dog(10, 16), [])

    def test_negative_n(self):
        # n âm -> invalid
        self.assertEqual(calculate_chicken_and_dog(-1, 20), [])

    def test_negative_m(self):
        # m âm -> invalid
        self.assertEqual(calculate_chicken_and_dog(10, -4), [])

if __name__ == '__main__':
    unittest.main()
