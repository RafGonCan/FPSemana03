from collections import deque

num = input()
indiv = deque()
num = num.split()

for numero in num:
    indiv.append(numero)

print(indiv)

for quadrado in range(int(numero)):
    quadrados = int(indiv.pop())
    quadrados = quadrados*quadrados
    print(quadrados)