#******************************* Diccionario ******************************

print("Leyendo archivo...")
# Usamos encoding utf-8 para que lea los acentos (importante para italiano/francés)
arch = open("1.txt", "r", encoding="utf-8")
texto = arch.read()
arch.close()

# Alfabeto ajustado (incluimos acentos para no cortar palabras como 'città')
alfabeto = 'abcdefghijklmnopqrstuvwxyzàèéìòù'

texto = texto.lower()
destino = []

print("Limpiando texto...")
# Mantenemos la lógica del profesor: revisar letra por letra
for c in texto:
    if c in alfabeto:
        destino.append(c) # Usamos append porque es más rápido que sumar strings enormes
    else:
        destino.append(' ')

# Unimos los caracteres limpios
texto_limpio = "".join(destino)
datos = texto_limpio.split()

print("Generando lista de palabras únicas...")
# AQUI LA OPTIMIZACIÓN: 
# Usamos set() para eliminar repetidos instantáneamente.
# (El método "if p not in dic1" tardaría demasiado con 22k palabras)
dic1 = list(set(datos))
dic1.sort()

#******************************* Guardar Resultado ******************************
nombre_salida = "diccionario_completo.txt"
print(f"Escribiendo {len(dic1)} palabras en el archivo '{nombre_salida}'...")

# Guardamos en un archivo txt nuevo en lugar de solo imprimir
salida = open(nombre_salida, "w", encoding="utf-8")
salida.write(f"Total de palabras únicas: {len(dic1)}\n")
salida.write("========================================\n")

for palabra in dic1:
    salida.write(palabra + "\n")

salida.close()

print("¡Proceso terminado! Revisa el archivo 'diccionario_completo.txt'.")
