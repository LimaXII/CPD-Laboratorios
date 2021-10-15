#Laboratorio 4 CPD - Tabelas Hash (Enderecamento fechado)
#Nomes: Luccas da Silva Lima e Bruno Longo Farina
#Turma: B

#-----------------------------------------------------------------------------------------------------------------
##Usar a forma polinomial. p = 31 (primeiro numero primo maior que 26, dado que 26 corresponde a letra 'z')
##Usar o metodo de Horner.
##O arquivo de entrar possui 10000 nomes. Vamos precisar criar 4 tabelas hash de diferentes tamanhos
## M = 503, 2503, 5003 e 7507.
##Para essas 4 tabelas, todos so 10000 nomes devem ser inseridos
##Depois precisa consultar alguns nomes, usando o arquivo consultas.txt
#-----------------------------------------------------------------------------------------------------------------

#Funcao que cria a tabela hash.
def hash_table(contents, M, vet):
    #Variavel que ira guardar o numero correspondente a cada nome    
    for x in range (0, 10000): 
                        #Percorre todas os nomes da lista.                
        hash = horner_method(contents[x], M)      #Chama a funcao do metodo de Horner, para achar uma posicao adequada para o nome na tabela hash.                               
        hash_insert(hash, vet,contents[x])                    #Chama a funcao que ira inserir os nomes na tabela hash.

#Funcao que calcula o valor do polinomio especifico, dado um nome.
def horner_method(word, M):
    p = 31                                     #Primeiro numero primo maior que 26.
    hash = 0 
                                     #Hash comeca valendo 0.
    for i in word:                         #Percorre a palavra.
        if ((i != '\n') and (i != ' ')):       #Testa se o char eh diferente de \n e "espaco".
            num = ord(i)                       #Caso seja diferente, transforma o char para int e acumula em uma soma.
            hash = (p * hash + num) % M        #Cria um polinomio correspondente a palavra.            
    return(hash)

#Insere o nome em uma determinada posicao da tabela.
def hash_insert(pos, vet,name):  
    #FAZE
    #nameaux=name[0:len(name)-1]
    #vet[pos].append(nameaux)
    vet[pos].append(name)
    return

def realizar_consulta(vet,name):
    aux=horner_method(name,len(vet))
    for i in range(0,len(vet[aux])):
        if(name==vet[aux][i]):
            return i+1
    return len(vet[aux])+1

#Abre e le o arquivo de nomes.
with open('nomes_10000.txt') as f:    #C:\\Users\\bruno\\OneDrive\\Documentos\\GitHub\\fafafa\\fafasfa\\Laboratório 4\\
    contents = f.readlines()          #Armazena cada nome em uma posicao do vetor contents.

#Abre e le o arquivo de consulta.
with open('consultas.txt') as f:    
    consult_contents = f.readlines()  #Armazena cada nome em uma posicao do vetor contents.

print(consult_contents)   
M = 503                               #Tamanho da primeira tabela hash a ser criada.
#---------
#Tem que arrumar essa declaracao de vetor.
#O certo seria criar um vetor com uma lista em cada posicao. Assim para o caso de colisoes, o valor
#seria colocado na sequencia da lista do determinado nodo do vetor.
vet = [[] for _ in range(0,M)]                              #Vetor que ira armazenar a tabela hash.
#---------
escrita=[]
hash_table(contents, M, vet)             #Chama a funcao para criar a tabela hash.

media=0
contador=0
maximo=0

for i in range(0,len(consult_contents)):
    aux=consult_contents[i][0:len(consult_contents[i])-1]
    numcons = realizar_consulta(vet,consult_contents[i])
    escrita.append(aux)
    escrita.append(" ")
    escrita.append(numcons)
    escrita.append('\n')
    media += numcons
    contador += 1
    if(numcons>maximo):
        maximo=numcons

media = media/contador
escrita.append("MEDIA ")
escrita.append(media)
escrita.append('\n')
escrita.append("MAXIMO ") #ver se o valor máximo é a soma de todas as consultas ou o nome que realizou mais consultas


########
########
########
########
########
########
########


escrita.append(maximo)
escrita.append('\n')

#isso aqui é só pra testar os valores e funções
#


arquivo = open('experimento503ponto2.txt', 'w')
for i in range(0,len(escrita)):
    arquivo.write(str(escrita[i]))    
#Fecha o arquivo
arquivo.close()
