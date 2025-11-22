import matplotlib.pyplot as plt

# 1. Lectura del archivo
print("Leyendo archivo...")
with open("pruebait.txt", "r", encoding="utf-8") as arch:
    texto = arch.read()

# 2. Definición del alfabeto (Ajustado para Italiano)
# Quitamos la 'ñ' y agregamos vocales acentuadas comunes en italiano
alfabeto = 'abcdefghijklmnopqrstuvwxyzàèéìòù' 

texto = texto.lower()

# ******************************* Histograma ******************************
print("Generando histograma...")
histo = {c: 0 for c in alfabeto}

for c in texto:
    if c in alfabeto:
        histo[c] += 1

# Ordenamos de mayor a menor frecuencia
histo_ord = dict(sorted(histo.items(), key=lambda x: x[1], reverse=True))

# ******************************* Diccionario ******************************
print("Generando diccionario...")

# Limpieza del texto: Si no es letra del alfabeto, se vuelve espacio
destino = []
for c in texto:
    if c in alfabeto:
        destino.append(c)
    else:
        destino.append(' ')
        
# Unimos y separamos por espacios (es más rápido que concatenar strings grandes)
texto_limpio = "".join(destino)
datos = texto_limpio.split()

# OPTIMIZACIÓN: Usamos set() para eliminar repetidos instantáneamente
# Tu método anterior tardaba mucho comparando palabra por palabra.
dic1 = list(set(datos))
dic1.sort()

# ******************************* Salida a Archivo ******************************
nombre_archivo_salida = "diccionario_generado.txt"
print(f"Escribiendo resultados en {nombre_archivo_salida}...")

with open(nombre_archivo_salida, "w", encoding="utf-8") as f_salida:
    f_salida.write(f"Total de palabras únicas: {len(dic1)}\n")
    f_salida.write("========================================\n")
    # Escribimos cada palabra en una linea nueva
    for palabra in dic1:
        f_salida.write(palabra + "\n")

print("¡Proceso terminado!")

# Mostramos la gráfica al final
plt.bar(histo_ord.keys(), histo_ord.values())
plt.title("Frecuencia de Letras en Italiano")
plt.show()