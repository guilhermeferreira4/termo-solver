class Termo:
    def __init__(self, word: str) -> None:
        self.word = word
    
    def guess(self, guess: str) -> list[int]:
        return [
            2 if w == g else 1 if g in self.word else 0
            for w, g in zip(self.word, guess)
        ]
        