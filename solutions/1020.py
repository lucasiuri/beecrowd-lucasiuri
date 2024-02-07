# https://www.beecrowd.com.br/judge/en/problems/view/1020

# Read an integer value corresponding to a person's age (in days)
# and print it in years, months and days, followed by its respective
# message “ano(s)”, “mes(es)”, “dia(s)”.

# Note: only to facilitate the calculation, consider the whole year
# with 365 days and 30 days every month. In the cases of test there will
#  never be a situation that allows 12 months and some days, like 360, 363 or 364.
#  This is just an exercise for the purpose of testing simple mathematical reasoning.

# Input
# The input file contains 1 integer value.

# Output
# Print the output, like the following example.

conversion_table = [365, 30, 1]
n = int(input())
y_m_d = []

for c in conversion_table:
    y_m_d.append(n // c)
    n = n % c

print(f'{y_m_d[0]} ano(s)')
print(f'{y_m_d[1]} mes(es)')
print(f'{y_m_d[2]} dia(s)')