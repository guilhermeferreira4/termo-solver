import random
import unicodedata
import os

def normalize_word(text: str) -> str:
    """Lowercase and remove accents/punctuation"""
    return unicodedata.normalize('NFKD', text.lower()).encode('ascii', 'ignore').decode('ascii')

class Termo:
    def __init__(self, word: str = None) -> None:
        if word is None:
            file_path = os.path.join(os.path.dirname(__file__), 'cinco_letras.txt')
            with open(file_path, 'r', encoding='utf-8') as f:
                words = [line.strip() for line in f if line.strip()]
            self.word = random.choice(words)
        else:
            self.word = word

    def guess(self, guess: str) -> list[int]:
        norm_word = normalize_word(self.word)
        norm_guess = normalize_word(guess)
        
        return [
            2 if w == g else 1 if g in norm_word else 0
            for w, g in zip(norm_word, norm_guess)
        ]

def filter_words(word_list: list[str], guess: str, result: list[int]) -> list[str]:
    return [word for word in word_list if Termo(word).guess(guess) == result]

def score_letters(word_list: list[str]) -> dict[str, int]:
    """
    Counts the frequency of each letter across the remaining valid words.
    Repeated characters in a single word only count once.
    """
    freq = {}
    for word in word_list:
        norm_word = set(normalize_word(word))
        for char in norm_word:
            freq[char] = freq.get(char, 0) + 1
    return freq

def sort_words_by_score(word_list: list[str]) -> list[str]:
    """
    Sorts a list of words in descending order based on their score.
    A word's score is the sum of the frequencies of its unique letters.
    """
    freq = score_letters(word_list)
    
    def get_score(word: str) -> int:
        norm_chars = set(normalize_word(word))
        return sum(freq.get(char, 0) for char in norm_chars)
        
    return sorted(word_list, key=lambda w: (-get_score(w), w))