# https://www.beecrowd.com.br/judge/en/problems/view/1021

# Read a value of floating point with two decimal places. This represents a monetary value.
#  After this, calculate the smallest possible number of notes and coins on which the value
#  can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins
#  are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list
#  of notes and the message “MOEDAS:” followed by the list of coins.

# Input
# The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

# Output
# Print the minimum quantity of banknotes and coins necessary to change the initial value,
# as the given example.

from decimal import *

NOTE_VALUES = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
COIN_VALUES = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

notes = {}
coins = {}

n = float(input())

for note in NOTE_VALUES:
    notes[note] = int(Decimal(str(n)) // Decimal(str(note)))
    n = float(Decimal(str(n)) % Decimal(str(note)))

for coin in COIN_VALUES:
    coins[coin] = int(Decimal(str(n)) // Decimal(str(coin)))
    n = float(Decimal(str(n)) % Decimal(str(coin)))


print('NOTAS:')
for k, v in notes.items():
    print(f'{v:.0f} nota(s) de R$ {k:.2f}')

print('MOEDAS:')
for k, v in coins.items():
    print(f'{v:.0f} moeda(s) de R$ {k:.2f}')
