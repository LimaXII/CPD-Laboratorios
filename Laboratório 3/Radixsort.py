#Laboratorio 3 CPD - Radix sort 
#Nomes: Luccas da Silva Lima e Bruno Longo Farina
#Turma: B

#Considere apenas as palavras contendo pelo menos 4 caracteres e apenas 
#letras do alfabeto ingles, isto e, ignore numerais e simbolos.
#variavel que vai armazenar o texto.

#O texto vai ser um vetor e cada palavra sera um nodo do vetor.
texto_completo = []

max_size = [0]

#Essa funcao deleta do texto todas as palavras com menos de 4 letras
#e todas as strings que nao contem letras do alfabeto ingles
def deletext(texto,max_size):
    texto_real = []
    for i in range(0, len(texto)):
        #Remove as palavras menore do que 4 letras
        if (len(texto[i]) >= 4):            
            if(len(texto[i]) > max_size[0]):
                max_size[0] = len(texto[i])                        
            texto_real.append(texto[i])
    texto.clear()
    for i in range(0,len(texto_real)):
        texto.append(texto_real[i])   

#Funcao que ordena o vetor de caracteres
def organizatext(texto,max_size):
    texto_aux = [[] for _ in range (0,len(texto))]
    for i in range(0,len(texto)):
        texto_aux[i] = texto[i]
    
    for a in range(0,max_size[0]):
        #cria um array auxiliar com dois parametros pra fazer o radix sort
        array_aux = [[[] for _ in range (0,len(texto_aux))] for _ in range (0,28)]
        #zera os indicadores para cada letra avaliada (AA significa que a palavra é menor do que a posição do termo avaliado)
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
        #para cada palavra no texto
        for i in range(0,len(texto_aux)):
            #verifica se a posição da letra analisada é vazia
            if(len(texto_aux[i]) < (max_size[0] - a)):
                array_aux[0][AA] = (texto_aux[i])
                AA += 1
            #senão põe em um array referente à letra analisada
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
        p = 0
        #para cada valor existente nos arrays adiciona a palavra no seu lugar correspondente no array auxiliar, substituindo o valor anterior
        for k in range(0,len(array_aux)):
            for l in range(0,len(array_aux[k])):
                if(array_aux[k][l] != []):
                    texto_aux[p] = array_aux[k][l] 
                    p += 1                    
        #depois de passados todos os valores, dá um clear no texto passado e poe o texto auxiliar no texto    
    texto.clear()    
    for i in range(0, len(texto_aux)):
        texto.append(texto_aux[i])        

#Funcao que ajeita a string que ira ser colocada nos arquivos                
def ajeitaTudo(texto):
    texto_real_oficial = []   
    palavraContando = 'sla'
    contador = 0
    for i in range(0,len(texto)):
        if(texto[i]==palavraContando):
            contador += 1   
        else:
            if(palavraContando != 'sla'):
                texto_real_oficial.append(palavraContando)
                texto_real_oficial.append(' ')
                texto_real_oficial.append(str(contador))
                texto_real_oficial.append('\n')            
            palavraContando = texto[i]
            contador = 1
    texto_real_oficial.append(palavraContando)
    texto_real_oficial.append(' ')
    texto_real_oficial.append(str(contador))
    texto_real_oficial.append('\n')     
    texto.clear()
    for i in range(0, len(texto_real_oficial)):
        texto.append(texto_real_oficial[i])
    
#Funcao main:
#Ordenando o arquivo Frankestein

#Abre e le o arquivo inteiro
with open('frankestein_clean.txt','r') as f: 
    data = f.readline()    
    texto = [str(i) for i in data.split()] 


#Chama a funcao para deletar todas as palavras com menos que 4 letras do texto
deletext(texto,max_size)

#Chama a funcao para ordernar o vetor de caracteres
organizatext(texto,max_size)

#Ajeita a string a ser colocada no arquivo
ajeitaTudo(texto)

#Cria o arquivo frankestein_ordenado.txt
arquivo = open('frankenstein_ordenado.txt', 'w')
j = 0
i = 0

#Escreve no arquivo o conteudo do vetor texto
for i in texto:
    arquivo.write(texto[j])        
    j=j+1
#Fecha o arquivo
arquivo.close()

#Ordenando o arquivo war and peace
with open('war_and_peace_clean.txt','r') as f: 
    data = f.readline()    
    texto = [str(i) for i in data.split()] 

#Chama a funcao para deletar todas as palavras com menos que 4 letras do texto.
deletext(texto,max_size)

#Chama a funcao para ordernar o vetor de caracteres
organizatext(texto,max_size)

#Ajeita a string a ser colocada no arquivo
ajeitaTudo(texto)

#Cria o arquivo war_and_peace_ordenado.txt
arquivo = open('war_and_peace_ordenado.txt', 'w')
j = 0
i = 0

#Escreve no arquivo o conteudo do vetor texto
for i in texto:
    arquivo.write(texto[j])    
    j=j+1
#Fecha o arquivo
arquivo.close()