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
        self.assertEqual(game.guess("pears"), [1, 1, 1, 0, 0])

    def test_mixed_match(self):
        game = Termo("apple")
        self.assertEqual(game.guess("ample"), [2, 0, 2, 2, 2])

    def test_wrong_spot_and_correct_spot(self):
        game = Termo("world")
        self.assertEqual(game.guess("water"), [2, 0, 0, 0, 1])

    def test_random_word_instantiation(self):
        game = Termo()
        self.assertIsNotNone(game.word)
        self.assertIsInstance(game.word, str)
        self.assertTrue(len(game.word) > 0)

    def test_ignore_accents_in_guess(self):
        game = Termo("ações")
        # should match perfectly regardless of accents
        self.assertEqual(game.guess("acoes"), [2, 2, 2, 2, 2])
        self.assertEqual(game.guess("áções"), [2, 2, 2, 2, 2])

    def test_ignore_accents_in_word(self):
        game = Termo("acoes")
        self.assertEqual(game.guess("ações"), [2, 2, 2, 2, 2])

    def test_case_insensitivity(self):
        game = Termo("Açude")
        self.assertEqual(game.guess("aCUdE"), [2, 2, 2, 2, 2])

if __name__ == "__main__":
    unittest.main()
