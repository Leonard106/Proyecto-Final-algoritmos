#******************************* Histograma ******************************
import matplotlib.pyplot as plt

arch = open("1.txt", "r", encoding="utf-8")
texto = arch.read()
arch.close()

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

texto = texto.lower()
histo = {c: 0 for c in alfabeto}

for c in texto:
    if c in alfabeto:
        histo[c] += 1

histo_ord = dict(sorted(histo.items(), key=lambda x: x[1], reverse=True))

print(histo_ord)

plt.bar(histo_ord.keys(), histo_ord.values())
plt.show()


#******************************* Diccionario ******************************


destino = ''
for c in texto:
    if c in alfabeto:
        destino += c
    else:
        destino += ' '

datos = destino.split()

dic1 = []
for p in datos:
    if p not in dic1:
        dic1.append(p)

dic1.sort()
print(dic1)
print(len(dic1))
