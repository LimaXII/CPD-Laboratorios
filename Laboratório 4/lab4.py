#Laboratorio 4 CPD - Tabelas Hash (Enderecamento fechado)
#Nomes: Luccas da Silva Lima e Bruno Longo Farina
#Turma: B

#Funcao que cria a tabela hash.
def hash_table(contents, M, vet):
    #Variavel que ira guardar o numero correspondente a cada nome    
    for x in range (0, 10000):                    #Percorre todas os nomes da lista.                
        hash = horner_method(contents[x], M)      #Chama a funcao do metodo de Horner, para achar uma posicao adequada para o nome na tabela hash.                               
        hash_insert(hash, vet,contents[x])        #Chama a funcao que ira inserir os nomes na tabela hash.

#Funcao que calcula o valor do polinomio especifico, dado um nome.
def horner_method(word, M):
    p = 31                                        #Primeiro numero primo maior que 26.
    hash = 0                                      #Hash comeca valendo 0.
    for i in word:                                #Percorre a palavra.
        if ((i != '\n') and (i != ' ')):          #Testa se o char eh diferente de \n e "espaco".
            num = ord(i)                          #Caso seja diferente, transforma o char para int e acumula em uma soma.
            hash = (p * hash + num) % M           #Cria um polinomio correspondente a palavra.            
    return(hash)

#Insere o nome em uma determinada posicao da tabela.
def hash_insert(pos, vet, name):     
    vet[pos].append(name)
    return

#Funcao que realiza a consulta de um nome na lista.
def realizar_consulta(vet,name):
    aux=horner_method(name,len(vet))
    for i in range(0,len(vet[aux])):
        if(name==vet[aux][i]):
            return i+1
    return -1

#Funcao que cria todos os arquivos de saida.
def cria_arquivo(M):      
    nome = ('experimento' + str(M) + '.txt')
    arquivo = open(nome, 'w')
    for i in range(0,len(escrita)):
        arquivo.write(str(escrita[i]))
    arquivo.close() 

def cria_texto():
    media = 0
    contador = 0
    maximo = 0
    for i in range(0,len(consult_contents)):
        numcons = realizar_consulta(vet,consult_contents[i])
        if(numcons>maximo):
            maximo=numcons
    maismax=maximo + 1
    for i in range(0,len(consult_contents)):
        aux=consult_contents[i][0:len(consult_contents[i])-1]
        numcons = realizar_consulta(vet,consult_contents[i])
        escrita.append(aux)
        escrita.append(" ")
        if(numcons == -1):
            escrita.append(maismax)
        else:
            escrita.append(numcons)
        escrita.append('\n')
        if(numcons == -1):
            media += maismax
        else:
            media += numcons
        contador += 1

    media = media/contador
    escrita.append("MEDIA ")
    escrita.append(media)
    escrita.append('\n')
    escrita.append("MAXIMO ") 
    escrita.append(maximo)
    escrita.append('\n')

#Abre e le o arquivo de nomes.
with open('C:\\Users\\bruno\\OneDrive\\Documentos\\GitHub\\fafafa\\fafasfa\\Laboratório 4\\nomes_10000.txt') as f:       #C:\\Users\\bruno\\OneDrive\\Documentos\\GitHub\\fafafa\\fafasfa\\Laboratório 4\\
    contents = f.readlines()             #Armazena cada nome em uma posicao do vetor contents.

#Abre e le o arquivo de consulta.
with open('C:\\Users\\bruno\\OneDrive\\Documentos\\GitHub\\fafafa\\fafasfa\\Laboratório 4\\consultas.txt') as f:    
    consult_contents = f.readlines()     #Armazena cada nome em uma posicao do vetor contents.

#Tabela Hash com M = 503.   
M = 503                                  #Tamanho da primeira tabela hash a ser criada.
vet = [[] for _ in range(0,M)]           #Vetor que ira armazenar a tabela hash.
escrita = []                             #Variavel que ira armazenar a escrita.
hash_table(contents, M, vet)             #Chama a funcao para criar a tabela hash.
cria_texto()                             #Chama a funcao para criar o texto de saida
cria_arquivo(M)                          #Chama a funcao para criar os arquivos de saida

#Tabela Hash com M = 2503. 
M = 2503                                 
vet = [[] for _ in range(0,M)]
escrita = []
hash_table(contents, M, vet)
cria_texto()                             #Chama a funcao para criar o texto de saida
cria_arquivo(M)                          #Chama a funcao para criar os arquivos de saida

#Tabela Hash com M = 5003. 
M = 5003
vet = [[] for _ in range(0,M)]
escrita = []
hash_table(contents, M, vet)
cria_texto()                             #Chama a funcao para criar o texto de saida
cria_arquivo(M)                          #Chama a funcao para criar os arquivos de saida

#Tabela Hash com M = 7507. 
M = 7507
vet = [[] for _ in range(0,M)]
escrita = []
hash_table(contents, M, vet)
cria_texto()                             #Chama a funcao para criar o texto de saida
cria_arquivo(M)                          #Chama a funcao para criar os arquivos de saida 