# https://www.beecrowd.com.br/judge/en/problems/view/1018



# In this problem you have to read an integer value and calculate the
# smallest possible number of banknotes in which the value may be decomposed.
# The possible banknotes are 100, 50, 20, 10, 5, 2 and 1.
# Print the read value and the list of banknotes.

# Input
# The input file contains an integer value N (0 < N < 1000000).

# Output
# Print the read number and the minimum quantity of each necessary
# banknotes in Portuguese language, as the given example.
# Do not forget to print the end of line after each line,
# otherwise you will receive “Presentation Error”.

value = int(input())
initial_value = value
notes_values = [100, 50, 20, 10, 5, 2, 1]
notes_qty = []

for note_value in notes_values:
    notes_qty.append(value // note_value)
    value = value % note_value

print(initial_value)
for i,n in enumerate(notes_qty):
    print(f'{n} nota(s) de R$ {notes_values[i]},00')
