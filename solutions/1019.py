# https://www.beecrowd.com.br/judge/en/problems/view/1019

# Read an integer value, which is the duration in seconds of a certain event
# in a factory, and inform it expressed in hours:minutes:seconds.

# Input
# The input file contains an integer N.

# Output
# Print the read time in the input file (seconds) converted in
# hours:minutes:seconds like the following example.

conversion_table = [3600, 60, 1]
n = int(input())
h_m_s = []

for c in conversion_table:
    h_m_s.append(n // c)
    n = n % c

for i, element in enumerate(h_m_s):
    if i == len(h_m_s)-1:
       print(f'{element}')
    else: 
        print(f'{element}:', end="")