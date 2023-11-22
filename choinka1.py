#importujemy biblioteki do kolorów i losowania
from termcolor import colored
import random
import os
import time

#oznaczyłem wysokość jako "h", ilość poziomów jako "lvl" oraz maksymalną 
#szerokość jako "mx_width" i odstep czasowy jako "delay"

lang = input("Please choose language/Proszę wybrać język: (pl/en) ")

if lang == "pl" or lang == "PL" or lang == "PL":
   h = int(input("Podaj wysokość choinki: "))
   lvl = int(input("Podaj ilość poziomów choinki: "))
   delay = int(input("Proszę podać odstęp czasowy: (w milisekundach)"))
elif lang == "en" or lang == "EN" or lang == "EN":
  h = int(input("Please enter height of tree: "))
  lvl = int(input("Please enter number of levels: "))
  delay = int(input("Please enter delay: (in miliseconds)"))
else:
  print("Zły język/Wrong Language")
  exit()

#wymierzamy maksymalną szerokość
mx_width = 2 * h * lvl - 1
colors = ['red', 'yellow', 'blue', 'magenta', 'cyan']

#funkcja rysująca choinkę
#"branch" oznacza gałęzie"

while True:
    for j in range(lvl):
        for i in range(h + j):
            branch = '*' * (2 * i + 1)
            branch = list(branch)
            for b in range(len(branch)):
                if random.randint(0, 3) == 0:  # Używamy funkcji random aby wylosować kolorową gałąź
                    branch[b] = colored(branch[b], random.choice(colors))
                else:
                    branch[b] = colored(branch[b], 'green')
            branch = ''.join(branch)
            print(' ' * ((mx_width - (2 * i + 1)) // 2) + branch)
    #Dodajemy konar
    for i in range(2):
        print(' ' * ((mx_width - 3) // 2) + '*' * 3)
    time.sleep(delay/100)  #Tu mamy odstęp czasowy
    os.system('cls' if os.name == 'nt' else 'clear')  #Tutaj czyścimy ekran konsoli 