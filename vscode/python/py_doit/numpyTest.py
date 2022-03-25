import scipy as sp
import numpy as np
import pandas as pd

discount = .05
cashflow = 100

def presentvalue(n) :
    return (cashflow / ((1 + discount)**n))

print(presentvalue(1))
print(presentvalue(2))

for i in range(20) :
    print(presentvalue(i))
    
loss = [-750, -250]
profit = [100] * 18
print(profit)

