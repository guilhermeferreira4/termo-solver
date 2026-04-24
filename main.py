from termo import Termo, filter_words, sort_words_by_score
import random
import os

def play_game(secret_word: str, all_words: list[str], initial_guess: str) -> int:
    termo = Termo(secret_word)
    valid_words = all_words.copy()
    
    tentativas = 1
    guess = initial_guess
    
    while True:
        guess_result = termo.guess(guess)
        
        if guess_result == [2, 2, 2, 2, 2]:
            return tentativas
            
        valid_words = filter_words(valid_words, guess, guess_result)
        
        if not valid_words:
            # Fallback for unexpected situations
            return tentativas
            
        sorted_words = sort_words_by_score(valid_words)
        guess = sorted_words[0]
        tentativas += 1

def main():
    file_path = os.path.join(os.path.dirname(__file__), 'cinco_letras.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        words = [line.strip() for line in f if line.strip()]

    print("Calculando a melhor palavra inicial...")
    initial_guess = sort_words_by_score(words)[0]
    print(f"Melhor palavra inicial: {initial_guess}")

    num_games = 100
    total_attempts = 0
    
    print(f"\nIniciando simulação de {num_games} jogos...")
    
    for i in range(num_games):
        secret_word = random.choice(words)
        attempts = play_game(secret_word, words, initial_guess)
        total_attempts += attempts
        
        if (i + 1) % 10 == 0:
            print(f"Progresso: {i + 1}/{num_games} jogos concluídos...")

    avg_attempts = total_attempts / num_games
    print(f"\nMédia de tentativas necessárias para vencer: {avg_attempts:.2f}")

if __name__ == "__main__":
    main()
