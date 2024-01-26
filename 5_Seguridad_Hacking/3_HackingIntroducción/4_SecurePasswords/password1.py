from random import choice

longitud = 8

valores = "0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ<=>@#%&+{|}[]~"

p = ""
p = p.join([choice(valores) for i in range(longitud)])

print(p)