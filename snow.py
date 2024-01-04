import os 
import random 
import time 

# Define a largura e a altura do terminal
WIDTH = 80
HEIGHT = 24

# Cria uma lista para armazenar os flocos de neve
snowflakes = [' ' for _ in range(WIDTH * HEIGHT)]

while True:
    # Limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Move cada floco de neve para baixo
    for i in range(WIDTH * HEIGHT - 1, WIDTH - 1, -1):
        snowflakes[i] = snowflakes[i - WIDTH]

    # Adiciona novos flocos de neve no topo
    for i in range(WIDTH):
        snowflakes[i] = '*' if random.random() < 0.1 else ' '

    # Imprime os flocos de neve
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(snowflakes[x + y * WIDTH], end='')
        print()

    # Pausa por um curto período de tempo
    time.sleep(0.1) 