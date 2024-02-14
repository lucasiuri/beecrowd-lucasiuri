# # https://judge.beecrowd.com/en/problems/view/1022

# You were invited to do a little job for your Mathematic teacher.
#  The job is to read a Mathematic expression in format of two rational
# numbers (numerator / denominator) and present the result of the operation.
# Each operand or operator is separated by a blank space.
# The input sequence (each line) must respect the following format:
# number, (‘/’ char), number, operation char (‘/’, ‘*’, ‘+’, ‘-‘), number, (‘/’ char), number.
# The answer must be presented followed by ‘=’ operator and the simplified answer.
# If the answer can’t be simplified, it must be repeated after a ‘=’ operator.

# Considering N1 and D1 as numerator and denominator of the first fraction,
# follow the orientation about how to do each one of these 4 operations:

# Sum: (N1*D2 + N2*D1) / (D1*D2)
# Subtraction: (N1*D2 - N2*D1) / (D1*D2)
# Multiplication: (N1*N2) / (D1*D2)
# Division: (N1/D1) / (N2/D2), that means (N1*D2)/(N2*D1)

# Input
# The input contains several cases of test. The first value is an integer N (1 ≤ N ≤ 1*104),
# indicating the amount of cases of test that must be read. Each case of test contains
# a rational value X (1 ≤ X ≤ 1000), an operation (-, +, * or /) and another rational
# value Y (1 ≤ Y ≤ 1000).

# Output
# The output must be a rational number, followed by a “=“ sign and another rational number,
# that is the simplification of the first value. In case of the first value can’t be simplified,
# the same value must be repeated after the ‘=’ sign.

def euclid_gcd(N,D):
    if D == 0:
        return N
    else:
        return euclid_gcd(D, N % D)

def simplify(expression):
    expression = expression.split('/')
    N = int(expression[0])
    D = int(expression[1])

    gcd = euclid_gcd(N,D)

    return str(int(N/gcd))+'/'+str(int(D/gcd))

n = int(input())
results = []

for _ in range(n):
    expression = input().split()
    N1 = int(expression[0])
    D1 = int(expression[2])
    N2 = int(expression[4])
    D2 = int(expression[6])

    if expression[3] == '+':
        result = str(N1*D2+N2*D1)+'/'+ str(D1*D2)
    
    elif expression[3] == '-':
        result = str(N1*D2-N2*D1)+'/'+ str(D1*D2)
    
    elif expression[3] == '*':
        result = str(N1*N2)+'/'+ str(D1*D2)
    
    elif expression[3] == '/':
        result = str(N1*D2)+'/'+ str(N2*D1)
    

    
    
    result += " = " + simplify(result)
    results.append(result)

for r in results:
    print(r)

