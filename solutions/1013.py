# https://www.beecrowd.com.br/judge/en/problems/view/1013

# Make a program that reads 3 integer values and present the greatest one
# followed by the message "eh o maior". Use the given formula.

# Input
# The input file contains 3 integer values.

# Output
# Print the greatest of these three values followed by a space and the message “eh o maior”.

a, b, c = map(int, input().split())

maiorAB = (a+b+abs(a-b))/2
maior = int((maiorAB+c+abs(maiorAB-c))/2)

print(f'{maior} eh o maior')