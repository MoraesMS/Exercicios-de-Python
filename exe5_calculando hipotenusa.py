from math import hypot
co = float(input('Comprimento do cateto Oposto: '))
ca = float(input('Comprimento do cateto Adjacente: '))
#h = (co ** 2 + ca ** 2) ** (1/2)
h = hypot(co, ca)
print(f'A Hipotenusa vai mediar {h:.2f}.')
