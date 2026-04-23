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

    def test_filter_words(self):
        from termo import filter_words
        word_list = ["apple", "ample", "apply", "peach", "maple"]
        # With current guess logic, Termo("ample").guess("apple") returns [2, 1, 2, 2, 2]
        self.assertEqual(filter_words(word_list, "apple", [2, 1, 2, 2, 2]), ["ample"])

        # Termo("ample").guess("peach") returns [1, 1, 1, 0, 0]
        # But so does Termo("apple") and Termo("maple")
        self.assertEqual(filter_words(word_list, "peach", [1, 1, 1, 0, 0]), ["apple", "ample", "maple"])

    def test_score_letters(self):
        from termo import score_letters
        word_list = ["mamao", "papel"]
        # mamao -> m, a, o
        # papel -> p, a, e, l
        # a: 2, m: 1, o: 1, p: 1, e: 1, l: 1
        expected = {'a': 2, 'm': 1, 'o': 1, 'p': 1, 'e': 1, 'l': 1}
        self.assertEqual(score_letters(word_list), expected)

    def test_score_letters_with_accents(self):
        from termo import score_letters
        word_list = ["Ações", "Ábaco"]
        # acoes -> a, c, o, e, s
        # abaco -> a, b, c, o
        # a: 2, c: 2, o: 2, e: 1, s: 1, b: 1
        expected = {'a': 2, 'c': 2, 'o': 2, 'e': 1, 's': 1, 'b': 1}
        self.assertEqual(score_letters(word_list), expected)

    def test_sort_words_by_score(self):
        from termo import sort_words_by_score
        word_list = ["mamao", "papel", "meloa"]
        # Frequencies:
        # m: 2, a: 3, o: 2, p: 1, e: 2, l: 2
        # Scores (unique letters only):
        # mamao: m(2) + a(3) + o(2) = 7
        # papel: p(1) + a(3) + e(2) + l(2) = 8
        # meloa: m(2) + e(2) + l(2) + o(2) + a(3) = 11
        # Expected sort: meloa (11), papel (8), mamao (7)
        self.assertEqual(sort_words_by_score(word_list), ["meloa", "papel", "mamao"])

if __name__ == "__main__":
    unittest.main()
