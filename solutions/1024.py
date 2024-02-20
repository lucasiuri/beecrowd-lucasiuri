# https://judge.beecrowd.com/en/problems/view/1024



# You have been asked to build a simple encryption program. This program
# should be able to send coded messages without someone been able to read them.
# The process is very simple. It is divided into two parts.

# First, each uppercase or lowercase letter must be shifted three
# positions to the right, according to the ASCII table: letter 'a'
# should become letter 'd', letter 'y' must become the character '|'
# and so on. Second, each line must be reversed. After being reversed,
# all characters from the half on (truncated) must be moved one position
# to the left in ASCII. In this case, 'b' becomes 'a' and 'a' becomes '`'.

# For example, if the resulting word of the first part is "tesla",
# the letters "sla" should be moved one position to the left.
# However, if the resulting word of the first part is "t#$A", 
# the letters "$A" are to be displaced.

# Input
# The input contains a number of cases of test. The first line of 
# each case of test contains an integer N (1 ≤ N ≤ 1 * 10⁴),
# indicating the number of lines the problem should encrypt.
# The following N lines contain M characters each M (1 ≤ M ≤ 1 * 10³).

# Output
# For each input, you must present the encrypted message.

from math import floor

def shift_ascii(character, n_positions):
    return chr(ord(character)+n_positions)

def encrypt(word):
    encrypted = []
    for i, c in enumerate(word):
        if c.isalpha():
            encrypted.append(shift_ascii(c, 3))
        else:
            encrypted.append(c)
    encrypted = encrypted[::-1]
    index = floor(len(encrypted)/2)
    for i in range(index, len(encrypted)):
        encrypted[i] = shift_ascii(encrypted[i], -1)
    
    return ''.join(encrypted)

n = int(input())
for _ in range(n):
    msg = input()
    print(encrypt(msg))
