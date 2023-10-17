import unicodedata
import sys

# Pobierz emoji od użytkownika jako ciąg znaków
em = input('Wprowadź emoji: ')

# Zwróć zakodowaną nazwę emoji na podstawie metadanych
print(unicodedata.name(em[0]))

# Zakończ działanie programu
sys.exit()