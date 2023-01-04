from random import *
from lib import *
from pandas import *

c = randint(1,10)
a = randint(1,10)
b = randint(1,10)

d = delta(a,b,c)
if d > 0:
    print("Delta Positif")

else:
    print("Delta négatif ou nul")