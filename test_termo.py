import unittest
from termo import Termo

class TestTermo(unittest.TestCase):
    def test_exact_match(self):
        game = Termo("apple")
        self.assertEqual(game.guess("apple"), [2, 2, 2, 2, 2])

    def test_completely_wrong(self):
        game = Termo("apple")
        self.assertEqual(game.guess("ghost"), [0, 0, 0, 0, 0])

    def test_partial_match(self):
        game = Termo("apple")
        # 'p' is in 'apple' but wrong spot -> 1
        # 'e' is in 'apple' but wrong spot -> 1
        # 'a' is in 'apple' but wrong spot -> 1
        # 'r' is not in 'apple' -> 0
        # 's' is not in 'apple' -> 0
        self.assertEqual(game.guess("pears"), [1, 1, 1, 0, 0])

    def test_mixed_match(self):
        game = Termo("apple")
        # 'a' is correct -> 2
        # 'm' is wrong -> 0
        # 'p' is correct -> 2
        # 'l' is correct -> 2
        # 'e' is correct -> 2
        self.assertEqual(game.guess("ample"), [2, 0, 2, 2, 2])

    def test_wrong_spot_and_correct_spot(self):
        game = Termo("world")
        # w -> correct (2)
        # a -> wrong (0)
        # t -> wrong (0)
        # e -> wrong (0)
        # r -> in word, wrong spot (1)
        self.assertEqual(game.guess("water"), [2, 0, 0, 0, 1])

if __name__ == "__main__":
    unittest.main()
