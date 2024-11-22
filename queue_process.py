from collections import deque

frase = input()
s_frase = frase.split()
plv = deque()

for letra in s_frase:
    plv.appendleft(letra)
print(plv)

for palavras in s_frase:
    if "o" in palavras:
        print(palavras)