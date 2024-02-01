# https://www.beecrowd.com.br/judge/en/problems/view/1010



# In this problem, the task is to read a code of a product 1, the number of units of product 1,
# the price for one unit of product 1, the code of a product 2, the number of units of product 2
#  and the price for one unit of product 2. After this, calculate and show the amount to be paid.

# Input
# The input file contains two lines of data. In each line there will be 3 values: two integers and a floating value with 2 digits after the decimal point.

# Output
# The output file must be a message like the following example where "Valor a pagar" means Value to Pay. Remember the space after ":" and after "R$" symbol. The value must be presented with 2 digits after the point.

def get_inputs():
    c, n, p = map(float, input().split())
    return c,n,p

code1, n1, price1 = get_inputs()
code2, n2, price2 = get_inputs()

print(f'VALOR A PAGAR: R$ {n1*price1+n2*price2:.2f}')