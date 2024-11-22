from collections import deque

num = input()
indiv = deque(int(numero) for numero in num.split())

print(indiv)

while indiv:
    numero = indiv.pop()
    print(numero**2)