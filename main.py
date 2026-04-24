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

def assistant_mode(words: list[str]):
    valid_words = words.copy()
    
    print("\n--- Modo Assistente do Termo ---")
    print("O assistente sugerirá a melhor palavra para você jogar.")
    print("Após jogar, digite o resultado que o jogo retornou.")
    print("Use 0 para cinza (não tem na palavra), 1 para amarelo (lugar errado) e 2 para verde (lugar certo).")
    print("Exemplo: se o resultado for 'cinza, amarelo, cinza, cinza, verde', digite 01002")
    
    tentativas = 1
    
    while True:
        if not valid_words:
            print("\nNão há mais palavras possíveis. Verifique se você digitou algum resultado errado.")
            break
            
        sorted_words = sort_words_by_score(valid_words)
        guess = sorted_words[0]
        
        print(f"\n--- Tentativa {tentativas} ---")
        print(f"Palavras possíveis restantes: {len(valid_words)}")
        if len(valid_words) <= 10:
            print(f"Palavras possíveis: {', '.join(sorted_words[:10])}")
        print(f"Sugestão de jogada: >> {guess.upper()} <<")
        
        while True:
            result_str = input("Qual foi o resultado (5 números de 0 a 2) ou 'q' para sair? ").strip()
            
            if result_str.lower() == 'q':
                return
                
            if len(result_str) == 5 and all(c in '012' for c in result_str):
                break
            print("Entrada inválida. Digite exatamente 5 números (0, 1 ou 2).")
            
        result = [int(c) for c in result_str]
        
        if result == [2, 2, 2, 2, 2]:
            print(f"\nParabéns! A palavra era '{guess.upper()}'. Vencemos em {tentativas} tentativas!")
            break
            
        valid_words = filter_words(valid_words, guess, result)
        tentativas += 1

def simulation_mode(words: list[str]):
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

def main():
    file_path = os.path.join(os.path.dirname(__file__), 'cinco_letras.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        words = [line.strip() for line in f if line.strip()]

    print("Escolha o modo de execução:")
    print("1. Assistente (jogar o jogo real)")
    print("2. Simulação (testar o algoritmo)")
    
    choice = input("Opção (1 ou 2) [padrão: 1]: ").strip()
    
    if choice == '2':
        simulation_mode(words)
    else:
        assistant_mode(words)

if __name__ == "__main__":
    main()
