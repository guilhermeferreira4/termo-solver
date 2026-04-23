from termo import Termo, filter_words
import random
import os

def main():
    file_path = os.path.join(os.path.dirname(__file__), 'cinco_letras.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        words = [line.strip() for line in f if line.strip()]
    word = random.choice(words)

    print(f'A palavra do dia é \"{word}\"')

    termo = Termo(word)
    guess = 'talar'
    
    guess_result = termo.guess(guess)
    print(f'Resultado da tentativa "{guess}": {guess_result}')
    print(f'Palavras que servem: {filter_words(words, guess, guess_result)}')
    

if __name__ == "__main__":
    main()
