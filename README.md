# Termo Solver

A Python-based assistant and simulator for the game **Termo** (the Brazilian Portuguese version of Wordle).

*Read this in [Portuguese](#termo-solver-assistente-e-simulador) / Leia em [Português](#termo-solver-assistente-e-simulador)*

---

## English

### Features

This project uses a frequency-based scoring algorithm to suggest optimal guesses. It features two main execution modes:

#### 1. Assistant Mode (Play along)
Acts as your intelligent sidekick while you play the real game. 
- It analyzes a dictionary of Portuguese 5-letter words (`cinco_letras.txt`).
- It calculates letter frequencies across all valid remaining words to suggest the most mathematically optimal guess.
- After you input the guess into the real game, you feed the result back to the script using numbers:
  - `0` for gray (letter not in the word)
  - `1` for yellow (correct letter, wrong position)
  - `2` for green (correct letter, correct position)
- The assistant then filters the dictionary and suggests the next optimal word, repeating the process until you win.

#### 2. Simulation Mode (Testing)
Evaluates the algorithm's performance by running 100 automated games against randomly chosen secret words from the dictionary. It outputs the average number of attempts required for the algorithm to win.

### How to Run

1. Ensure you have Python installed (no external dependencies are required).
2. Make sure the word list file `cinco_letras.txt` is in the same directory.
3. Run the main script:
   ```bash
   python main.py
   ```
4. Choose the mode you want to execute (1 for Assistant, 2 for Simulation).

### Running Tests

To execute the unit tests and ensure the core logic works correctly:
```bash
python -m unittest test_termo.py
```

---

## Termo Solver (Assistente e Simulador)

Um assistente e simulador feito em Python para o jogo **Termo** (versão brasileira do Wordle).

### Funcionalidades

Este projeto utiliza um algoritmo de pontuação baseado na frequência das letras para sugerir jogadas ótimas. Ele possui dois modos principais de execução:

#### 1. Modo Assistente (Jogar junto)
Atua como um ajudante inteligente enquanto você joga o jogo real.
- Analisa um dicionário de palavras de 5 letras em português (`cinco_letras.txt`).
- Calcula a frequência das letras entre todas as palavras válidas restantes para sugerir a jogada matematicamente mais otimizada.
- Após você jogar a palavra no jogo real, você informa o resultado para o script usando números:
  - `0` para cinza (letra não existe na palavra)
  - `1` para amarelo (letra certa, lugar errado)
  - `2` para verde (letra certa, lugar certo)
- O assistente então filtra o dicionário e sugere a próxima melhor palavra, repetindo o processo até a vitória.

#### 2. Modo Simulação (Testes)
Avalia o desempenho do algoritmo executando 100 jogos automáticos contra palavras secretas escolhidas aleatoriamente do dicionário. Ele retorna a média de tentativas que o algoritmo levou para vencer.

### Como Executar

1. Certifique-se de ter o Python instalado (nenhuma biblioteca externa é necessária).
2. Garanta que o arquivo `cinco_letras.txt` esteja no mesmo diretório.
3. Execute o script principal:
   ```bash
   python main.py
   ```
4. Escolha o modo que deseja executar (1 para Assistente, 2 para Simulação).

### Executando os Testes

Para executar os testes unitários e garantir que a lógica principal está funcionando corretamente:
```bash
python -m unittest test_termo.py
```
