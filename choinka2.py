#importujemy biblioteki do kolorów i losowania
from termcolor import colored
import random
import os
import time

print("Zalecane jest aby nie podawać odstępu czasowego mniejszego niż 40")
print("______________________")

wys = int(input("Wpisz wysokość jednego poziomu choinki: "))
poz = int(input("Wpisz ilość poziomów choinki: "))
odstęp = int(input("Wpisz odstęp czasowy między animowaniem choinki: (w milisekundach) "))

#wymierzamy maksymalną szerokość
max_szer = 2 * wys * poz - 1
kolory = ['red', 'yellow', 'blue', 'magenta', 'cyan']

#funkcja do rysowania choinki

while True:
    for j in range(poz):
        for i in range(wys - 1 + j):
            gałąź = '@' * (2 * i + 1)
            gałąź = list(gałąź)
            for b in range(len(gałąź)):
                if random.randint(0, 3) == 0:  # Używamy funkcji random aby wylosować kolorowy kawałek choinki
                    gałąź[b] = colored(gałąź[b], random.choice(kolory))
                else:
                    gałąź[b] = colored(gałąź[b], 'green')
            gałąź = ''.join(gałąź)
            print(' ' * ((max_szer - (2 * i + 1)) // 2) + gałąź)
    #Dodajemy pień
    if poz > 3:
      for i in range(3):
          print(colored(' ' * ((max_szer - 3) // 2) + '#' * 3, 'yellow'))
      time.sleep(odstęp/100)  #Tu mamy odstęp czasowy
      os.system('cls' if os.name == 'nt' else 'clear')  #Tutaj czyścimy ekran konsoli 
    else:
      for i in range(2):
        print(colored(' ' * ((max_szer - 3) // 2) + '#' * 3, 'yellow'))
        
        
      time.sleep(odstęp/100)  #Tu mamy odstęp czasowy
      
      os.system('cls' if os.name == 'nt' else 'clear')  #Tutaj czyścimy ekran konsoli 
