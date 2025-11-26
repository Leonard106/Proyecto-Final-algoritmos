import matplotlib.pyplot as plt

with open("C:\\Users\\fifac\\Downloads\\words.txt", "r", encoding="utf-8") as arch:
    texto_ing = arch.read().lower()

alfabeto = 'abcdefghijklmnopqrstuvwxyz' 

histo_ing = {l: 0 for l in alfabeto}
total_ing = 0
for letra in texto_ing:
    if letra in alfabeto:
        histo_ing[letra] += 1
        total_ing += 1

if total_ing > 0:
    for l in histo_ing:
        histo_ing[l] = (histo_ing[l] / total_ing) * 100

valores_ing = sorted(histo_ing.values(), reverse=True)

texto1 = """Kz amzmld, xjdxxm lmxxkaakm, st itz wktzzm tz otllmud, t xdamuit idwzk kuikskivk d idzzd ldwkmuk. Zt wmzt, kz sdufld d z'dxfldokft idzzt amit xmum hktuayd; bvdxf'vzfkot d zvuwt d pmzft. Kz ovxm d tzzvuwtfm d zd mldaaykd xmum flktuwmztlk di dxfldotodufd omhkzk. Umlotzodufd sksd ku amjjkt, amu k avaakmzk, tuayd xd ftzsmzft d jmxxkhkzd mxxdlstlud dxdojztlk xmzkftlk m ku wlvjjk ik bvtfflm m xdk tivzfk. Kz otxaykm otlaykt kz fdllkfmlkm ku omim xkxfdotfkam d amovukat amu k jlmjlk xkokzk tivzfk. Kz otxaykm otlaykt kz fdllkfmlkm ku omim xkxfdotfkam d amovukat amu k jlmjlk xkokzk tffltsdlxm xdwutzk xmumlk, skxksk, ftffkzk d mzptffksk. Vut smzjd jvm lkamumxadld vu tzflm dxdojztld itzz'mimld, mzfld t idakpltlud kz ltuwm wdltlaykam d kz zksdzzm xmaktzd. D xkwukpkatfksm xmffmzkudtld ayd, ku bvdxft xjdakd, zt amjjkt fduid t lkpmlotlxk mwuk tuum d ayd kz otxaykm xmzkftodufd jtlfdakjt tffkstodufd tzzt avlt d tzz'tzzdstodufm idzzt jlmzd, jlmavltuim kz akhm d ikpduiduim k avaakmzk it jmxxkhkzk jlditfmlk."""

texto2 = """J'zcikmg gyp jg lcfwp eg j'zcikmgc ezfr, fk icbcg hfw iuuicpwgkp if mgkcg Awpcfy eg ji lidwjjg Cfpiagiy. Eg yi azduzywpwzk kfpcwpwzkkgjjg, yg ewypwkmfg yi liwbjg oijgfc gkgcmgpwhfg, mciag i yi lzcpg pgkgfc gk gif gp yi cwangyyg gk owpidwkg A, gk iaweg lzjwhfg gp gk dwkgcifr azddg jg uzpiyywfd, jg dimkgywfd gp jg aijawfd, hfw yzkp i ugwkg ibyzcbgy uic j'zcmikwydg. Wj azkpwgkp egy hfikpwpgy iuucgawibjgy eg bgpi-aiczpgkg, cgyuzkyibjg eg yi azfjgfc ptuwhfg gp azkkf uzfc ygy uczucwgpgy ikpwzrteikpgy ; Gk ujfy egy iawegy dijwhfg, zrijwhfg, picpcwhfg gp awpcwhfg, ag egckwgc cgklzcag j'iapwzk eg ji owpidwkg A. Ji hfikpwpg eg lwbcgy gyp iuucgawibjg gp yg pczfog ucwkawuijgdgkp eiky ji uicpwg bjikang gkpcg ji ufjug gp j'gazcag, yi azkyzddipwzk liozcwyg ezka jg pcikywp wkpgypwkij. Ji owpidwkg A uicpwawug i ji lzcdipwzk ef azjjimgkg, egy zy gp egy egkpy, egy mjzbfjgy czfmgy gp liozcwyg j'ibyzcupwzk ef lgc egy ijwdgkpy gp ji cgywypikag ifr wklgapwzky."""

histo1 = {l: 0 for l in alfabeto}
total1 = 0
for letra in texto1.lower():
    if letra in alfabeto:
        histo1[letra] += 1
        total1 += 1

for l in histo1:
    histo1[l] = (histo1[l] / total1) * 100
valores1 = sorted(histo1.values(), reverse=True)

histo2 = {l: 0 for l in alfabeto}
total2 = 0
for letra in texto2.lower():
    if letra in alfabeto:
        histo2[letra] += 1
        total2 += 1

for l in histo2:
    histo2[l] = (histo2[l] / total2) * 100
valores2 = sorted(histo2.values(), reverse=True)

diferencia1 = 0
diferencia2 = 0

for i in range(len(valores_ing)):
    diferencia1 += abs(valores_ing[i] - valores1[i])
    diferencia2 += abs(valores_ing[i] - valores2[i])

print("Diferencia Texto 1 vs Ingles:", diferencia1)
if diferencia1 < 15:
    print("CONCLUSION: El Texto 1 SI parece Ingles.")
else:
    print("CONCLUSION: El Texto 1 NO se parece al Ingles.")

print("Diferencia Texto 2 vs Ingles:", diferencia2)
if diferencia2 < 10:
    print("CONCLUSION: El Texto 2 SI parece Ingles.")
else:
    print("CONCLUSION: El Texto 2 NO se parece al Ingles.")

plt.plot(valores_ing, color='red', marker='o', label='Referencia Ingles')
plt.plot(valores1, color='green', linestyle='--', label='Texto 1')
plt.plot(valores2, color='blue', linestyle='--', label='Texto 2')

plt.legend()
plt.title("Comparacion de Frecuencias")
plt.xlabel("Ranking")
plt.ylabel("Porcentaje")
plt.show()

destino = []
for c in texto_ing:
    if c in alfabeto:
        destino.append(c)
    else:
        destino.append(' ')

datos = "".join(destino).split()

dic1 = list(set(datos))
dic1.sort()

salida = open("diccionario_completo_Ing.txt", "w", encoding="utf-8")
salida.write(str(len(dic1)) + "\n")

for p in dic1:
    salida.write(p + "\n")

salida.close()