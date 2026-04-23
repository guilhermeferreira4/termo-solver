from termo import Termo, filter_words, score_letters, sort_words_by_score
import random
import os

def main():
    file_path = os.path.join(os.path.dirname(__file__), 'cinco_letras.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        words = [line.strip() for line in f if line.strip()]
    word = random.choice(words)

    termo = Termo(word)
    valid_words = words.copy()
    
    print("Bem-vindo ao Termo!")
    # print(f"(Dica para debugar: a palavra é '{word}')\n")
    print(f"Sugestões iniciais: {sort_words_by_score(valid_words)[:10]}\n")

    tentativas = 1
    while tentativas <= 6:
        guess = input(f"Tentativa {tentativas}/6: ").strip().lower()
        if len(guess) != 5:
            print("A palavra deve ter 5 letras.")
            continue
            
        guess_result = termo.guess(guess)
        print(f'Resultado: {guess_result}')
        
        if guess_result == [2, 2, 2, 2, 2]:
            print(f'\nParabéns! Você acertou a palavra "{word}"!')
            break
            
        valid_words = filter_words(valid_words, guess, guess_result)
        sorted_words = sort_words_by_score(valid_words)
        
        print(f'Palavras restantes: {len(valid_words)}')
        if valid_words:
            print(f'Melhores palavras para a próxima tentativa:\n{sorted_words[:10]}\n')
        else:
            print("Nenhuma palavra na lista atende aos critérios.")
            break
            
        tentativas += 1
    else:
        print(f'\nFim de jogo. A palavra era "{word}".')

if __name__ == "__main__":
    main()
