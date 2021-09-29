#Laboratorio 3 CPD - Radix sort 
#Nomes: Luccas da Silva Lima e Bruno Longo Farina
#Turma: B

#Considere apenas as palavras contendo pelo menos 4 caracteres e apenas 
#letras do alfabeto ingles, isto e, ignore numerais e simbolos.


#variavel que vai armazenar o texto.
#O texto vai ser um vetor e cada palavra sera um nodo do vetor.
texto_completo = []
texto_real = []
texto_real2 = []
max_size = [0]
texto_aux = []

#array_aux = [[[] for _ in range (0,28)] for _ in range (0,28)]


#Essa funcao deleta do texto todas as palavras com menos de 4 letras
#e todas as strings que nao contem letras do alfabeto ingles
def deletext(texto,max_size):
    for i in range(0, len(texto)):
        #Remove as palavras menore do que 4 letras
        if (len(texto[i]) >= 4):
            if(len(texto[i]) > max_size[0]):
                max_size[0] = len(texto[i])
            #Caso seja maior que 4, remove palavras que nao contem letras do alfabeto ingles
            if(texto[i] >= 'A' and texto[i] <= 'Z'):
                texto_real.append(texto[i])
                 

def organizatext(texto,max_size):
    texto_aux = texto
    for a in range(0,max_size[0]):
        array_aux = [[[] for _ in range (0,len(texto_aux))] for _ in range (0,28)]
        AA = 0
        A = 0
        B = 0
        C = 0
        D = 0
        E = 0
        F = 0
        G = 0
        H = 0
        I = 0
        J = 0
        K = 0
        L = 0
        M = 0
        N = 0
        O = 0
        P = 0
        Q = 0
        R = 0
        S = 0
        T = 0
        U = 0
        V = 0
        W = 0
        X = 0
        Y = 0
        Z = 0
        for i in range(0,len(texto_aux)):
            if(len(texto_aux[i]) < (max_size[0] - a)):
                array_aux[0][AA] = (texto_aux[i])
                AA += 1
            else:
                if(texto_aux[i][(max_size[0]-a-1)] == 'A'):
                    array_aux[1][A] = (texto_aux[i])
                    A += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'B'):
                    array_aux[2][B] = (texto_aux[i])
                    B += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'C'):
                    array_aux[3][C] = (texto_aux[i])
                    C += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'D'):
                    array_aux[4][D] = (texto_aux[i])
                    D += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'E'):
                    array_aux[5][E] = (texto_aux[i])
                    E += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'F'):
                    array_aux[6][F] = (texto_aux[i])
                    F += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'G'):
                    array_aux[7][G] = (texto_aux[i])
                    G += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'H'):
                    array_aux[8][H] = (texto_aux[i])
                    H += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'I'):
                    array_aux[9][I] = (texto_aux[i])
                    I += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'J'):
                    array_aux[10][J] = (texto_aux[i])
                    J += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'K'):
                    array_aux[11][K] = (texto_aux[i])
                    K += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'L'):
                    array_aux[12][L] = (texto_aux[i])
                    L += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'M'):
                    array_aux[13][M] = (texto_aux[i])
                    M += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'N'):
                    array_aux[14][N] = (texto_aux[i])
                    N += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'O'):
                    array_aux[15][O] = (texto_aux[i])
                    O += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'P'):
                    array_aux[16][P] = (texto_aux[i])
                    P += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'Q'):
                    array_aux[17][Q] = (texto_aux[i])
                    Q += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'R'):
                    array_aux[18][R] = (texto_aux[i])
                    R += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'S'):
                    array_aux[19][S] = (texto_aux[i])
                    S += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'T'):
                    array_aux[20][T] = (texto_aux[i])
                    T += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'U'):
                    array_aux[21][U] = (texto_aux[i])
                    U += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'V'):
                    array_aux[22][V] = (texto_aux[i])
                    V += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'W'):
                    array_aux[23][W] = (texto_aux[i])
                    W += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'X'):
                    array_aux[24][X] = (texto_aux[i])
                    X += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'Y'):
                    array_aux[25][Y] = (texto_aux[i])
                    Y += 1
                elif(texto_aux[i][(max_size[0]-a-1)] == 'Z'):
                    array_aux[26][Z] = (texto_aux[i])
                    Z += 1
        print(len(texto_aux))
        p = 0
        for k in range(0,len(array_aux)):
            for l in range(0,len(array_aux[k])):

                if(array_aux[k][l] != []):
                    texto_aux[p] = array_aux[k][l] 
                    p += 1
                    
        print("a = ", a)
    for i in range(0, len(texto_aux)):
        texto_real2.append(texto_aux[i])       

        
                
    





#Abre e le o arquivo inteiro.
with open('frankestein_clean.txt','r') as f: 
    data = f.readline()    
    texto = [str(i) for i in data.split()] 

#Chama a funcao para deletar todas as palavras com menos que 4 letras do texto.
deletext(texto,max_size)

organizatext(texto_real,max_size)

#So criei um arquivo para testar se o vetor texto realmente tava com o texto certinho.
arquivo = open('escrita_teste2.txt', 'w')
j = 0
i = 0

for i in texto_real2:
    arquivo.write(texto_real2[j])
    arquivo.write(' ')
    j=j+1
arquivo.close()



'''
if(len(texto[i]) < (max_size[0] - a)):
                array_aux[0].append(texto[i])
            else:
                if(texto[i][(max_size[0]-a-1)] == 'A'):
                    array_aux[1].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'B'):
                    array_aux[2].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'C'):
                    array_aux[3].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'D'):
                    array_aux[4].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'E'):
                    array_aux[5].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'F'):
                    array_aux[6].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'G'):
                    array_aux[7].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'H'):
                    array_aux[8].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'I'):
                    array_aux[9].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'J'):
                    array_aux[10].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'K'):
                    array_aux[11].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'L'):
                    array_aux[12].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'M'):
                    array_aux[13].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'N'):
                    array_aux[14].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'O'):
                    array_aux[15].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'P'):
                    array_aux[16].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'Q'):
                    array_aux[17].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'R'):
                    array_aux[18].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'S'):
                    array_aux[19].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'T'):
                    array_aux[20].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'U'):
                    array_aux[21].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'V'):
                    array_aux[22].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'W'):
                    array_aux[23].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'X'):
                    array_aux[24].append(texto[i])
                elif(texto[i][(max_size[0]-a-1)] == 'Y'):
                    array_aux[25].append(texto[i])'''