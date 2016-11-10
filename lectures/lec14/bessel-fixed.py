from scipy.misc import factorial as fact
from scipy.special import j0 as bessel

def term(m, x):
    return ((-1)**m)/(fact(m)*fact(m+1))*(0.5*x)**(2*m)

value = 0.5
max_term = 20
my_sum = 0.0
for i in range(0,max_term):
    my_sum += term(i, value)

print('series gives %f'%my_sum)
print('scipy gives %f'%bessel(value))
print('error is %f'%(my_sum-bessel(value)))
