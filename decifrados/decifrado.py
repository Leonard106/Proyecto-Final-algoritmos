def descifra_sustitucion(cadena, llave):
    alfabeto = 'abcdefghilmnopqrstuvxy' # 22 letras
    cifrado =  ''
    cadena = cadena.lower()    
    for letra in cadena:
        if letra in llave: 
            pos = llave.lower().index(letra)
            cifrado += alfabeto[pos]
        else:
            cifrado += letra        
    return cifrado

alfabeto = 'abcdefghilmnopqrstuvxy'
cifrado ="J'zcikmg gyp jg lcfwp eg j'zcikmgc ezfr, fk icbcg hfw iuuicpwgkp if mgkcg Awpcfy eg ji lidwjjg Cfpiagiy. Eg yi azduzywpwzk kfpcwpwzkkgjjg, yg ewypwkmfg yi liwbjg oijgfc gkgcmgpwhfg, mciag i yi lzcpg pgkgfc gk gif gp yi cwangyyg gk owpidwkg A, gk iaweg lzjwhfg gp gk dwkgcifr azddg jg uzpiyywfd, jg dimkgywfd gp jg aijawfd, hfw yzkp i ugwkg ibyzcbgy uic j'zcmikwydg. Wj azkpwgkp egy hfikpwpgy iuucgawibjgy eg bgpi-aiczpgkg, cgyuzkyibjg eg yi azfjgfc ptuwhfg gp azkkf uzfc ygy uczucwgpgy ikpwzrteikpgy ; Gk ujfy egy iawegy dijwhfg, zrijwhfg, picpcwhfg gp awpcwhfg, ag egckwgc cgklzcag j'iapwzk eg ji owpidwkg A. Ji hfikpwpg eg lwbcgy gyp iuucgawibjg gp yg pczfog ucwkawuijgdgkp eiky ji uicpwg bjikang gkpcg ji ufjug gp j'gazcag, yi azkyzddipwzk liozcwyg ezka jg pcikywp wkpgypwkij. Ji owpidwkg A uicpwawug i ji lzcdipwzk ef azjjimgkg, egy zy gp egy egkpy, egy mjzbfjgy czfmgy gp liozcwyg j'ibyzcupwzk ef lgc egy ijwdgkpy gp ji cgywypikag ifr wklgapwzky."
llave    = 'ibaeglmnwjdkzuhcypfort'

print(descifra_sustitucion(cifrado, llave))
'''
def carga_dic(nombre):
    arch = open(nombre, 'r')
    texto = arch.read()
    arch.close()
    return texto.split()

dic1 = carga_dic('./diccionario_completo_Fr.txt')

posA = 'c' #
posB = 'b' #
posC = 'r' #
posD = 'm' #
posE = 'd' #
posF = 'u' #
posG = 'e' #
posH = 'q' #
posI = 'a' #
posJ = 'l' #
posK = 'n' #
posL = 'f' #
posM = 'g' #
posN = 'h'
posO = 'v'
posP = 't' # *
posR = 'x' #
posT = 'y' #
posU = 'p' # 
posW = 'i' #
posY = 's' #
posZ = 'o' #

llave = 'abcdefghilmnopqrstuvxy'
llave = 'ibaeglmnwjdkzuhcypfort'


#probando con cifrado = zihbf 
#                       
#                                    
c = 0
prueba = 'mgkcg'
for p in dic1:
    if len(p) == 7 and len(set(p))== 7 :
        if p[0] in posB and p[1] in posJ and p[2] in posI  and p[3] in posK and p[4] in posA and p[5] in posN and p[6] in posG:# and p[7] in posW and p[8] in posH and p[9] in posF and p[10] in posG:
            
            
            print(p)
            if not(p[-1] in prueba):
                prueba += p[-1]
            c = c + 1
print('cumplen:', c)
print(prueba)


'''