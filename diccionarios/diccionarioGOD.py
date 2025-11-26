arch = open("diccionarios/diccionario_generado_It.txt", "r", encoding="utf-8")
texto = arch.read()
arch.close()

alfabeto = 'abcdefghijklmnopqrstuvwxyzàèéìòù'
texto = texto.lower()

destino = []
for c in texto:
    if c in alfabeto:
        destino.append(c)
    else:
        destino.append(' ')

datos = "".join(destino).split()

dic1 = list(set(datos))
dic1.sort()

salida = open("diccionario_completo.txt", "w", encoding="utf-8")
salida.write(str(len(dic1)) + "\n")

for p in dic1:
    salida.write(p + "\n")

salida.close()
