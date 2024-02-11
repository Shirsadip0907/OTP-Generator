import random
import math
d= '0123456789'
otp= ''
for i in range(0,4):
    otp+=d[math.floor(random.random()*10)]
print(otp)
