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
def hash_table(contents, vet):
    #Variavel que ira guardar o numero correspondente a cada nome    
    for x in range (0, 10000):                 #Percorre todas os nomes da lista.                
        hash = horner_method(contents[x])      #Chama a funcao do metodo de Horner, para achar uma posicao adequada para o nome na tabela hash.                               
        hash_insert(hash, vet)                 #Chama a funcao que ira inserir os nomes na tabela hash.

#Funcao que calcula o valor do polinomio especifico, dado um nome.
def horner_method(word):
    p = 31                                     #Primeiro numero primo maior que 26.
    hash = 0                                   #Hash comeca valendo 0.
    for i in word:                             #Percorre a palavra.
        if ((i != '\n') and (i != ' ')):       #Testa se o char eh diferente de \n e "espaco".
            num = ord(i)                       #Caso seja diferente, transforma o char para int e acumula em uma soma.
            hash = (p * hash + num) % M        #Cria um polinomio correspondente a palavra.            
    return(hash)

def hash_insert(pos, vet):  
    #FAZER!
    print('Precisa fazer')


#Abre e le o arquivo inteiro.
with open('nomes_10000.txt') as f:    
    contents = f.readlines()          #Armazena cada nome em uma posicao do vetor contents.

M = 503                               #Tamanho da primeira tabela hash a ser criada.

#---------
#Tem que arrumar essa declaracao de vetor, acho que ta errada ainda
vet = []                              #Vetor que ira armazenar a tabela hash.
#---------

hash_table(contents, vet)             #Chama a funcao para criar a tabela hash.