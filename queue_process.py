from collections import deque

frase = input()
plv = deque(frase.split())

print(plv)
for palavras in plv:
    if "o" in palavras:
        print(palavras)
        