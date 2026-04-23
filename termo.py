import random
import unicodedata
import os

class Termo:
    def __init__(self, word: str = None) -> None:
        if word is None:
            file_path = os.path.join(os.path.dirname(__file__), 'cinco_letras.txt')
            with open(file_path, 'r', encoding='utf-8') as f:
                words = [line.strip() for line in f if line.strip()]
            self.word = random.choice(words)
        else:
            self.word = word
            
    def _normalize(self, text: str) -> str:
        # Lowercase and remove accents/punctuation
        return unicodedata.normalize('NFKD', text.lower()).encode('ascii', 'ignore').decode('ascii')

    def guess(self, guess: str) -> list[int]:
        norm_word = self._normalize(self.word)
        norm_guess = self._normalize(guess)
        
        return [
            2 if w == g else 1 if g in norm_word else 0
            for w, g in zip(norm_word, norm_guess)
        ]

def filter_words(word_list: list[str], guess: str, result: list[int]) -> list[str]:
    """Filters a list of words, returning only those that match the given guess result."""
    return [word for word in word_list if Termo(word).guess(guess) == result]