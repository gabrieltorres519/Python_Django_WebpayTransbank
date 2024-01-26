from random import SystemRandom

longitud = 8

valores = "0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ<=>@#%&+{|}[]~"

cryptogen = SystemRandom()
p= ""

while longitud > 0:
    p = p + cryptogen.choice(valores)
    longitud = longitud-1

print(p)