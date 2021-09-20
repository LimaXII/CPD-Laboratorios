#Laboratorio 2 CPD - Quicksort 
#Nomes: Luccas da Silva Lima e Bruno Longo Farina
#Turma: B

#Biblioteca que gera numeros aleatorios
import random
import time
import statistics

#Funcao que seleciona a mediana entre 3 valores presentes no vetor (Valor inicial, final, e meio)
def part_mediana3(array, start, end):
    aux = [0,1,2]
    num = 0    
    for k in range(start,end):
        num = num + 1
    num = int(num / 2)
    mid = num + start     
    if (start == mid):  #Caso o array tenha so 2 elementos, retorna o primeiro
        return 0         
    #Primeiro valor do vetor
    aux[0] = array[start] 
    #Ultimo valor do vetor
    aux[1] = array[mid]
    #Valor do meio
    aux[2] = array[end]     

    #Calcula a mediana, utilizando a funcao statistics.median
    mediana = statistics.median(aux)   
    for i in range (start,end + 1):
        #Coloca o valor da mediana na primeira posicao do vetor
        if (mediana == array[i]):           
            auxiliar2 = array[start]            
            array[start] = mediana            
            array[i] = auxiliar2 

#Funcao que gera um particionador de forma aleatoria
def part_random(array, start, end):    
    #Gera um numero aleatorio que corresponde a uma posicao do array
    n = random.randint(start,end)
    #Troca o valor pela primeira posicao do vetor
    aux = array[start]
    array[start] = array[n]
    array[n] = aux

#Funcao Quicksort, utilizando o particionamento de Lomuto
def quicksort_lomuto_rnd(array, start, end, recursao, swaps):
    if(start < end):
        recursao[0] +=1

        part_random(array, start, end)
        q = lomuto(array, start, end, swaps)     
        quicksort_lomuto_rnd(array,start, q - 1, recursao, swaps)   #Ordena os elementos antes do particionador atual       
        quicksort_lomuto_rnd(array,q + 1, end, recursao, swaps)     #Ordena os elementos depois do particionador atual           

#Funcao Quicksort, utilizando o particionamento de Lomuto
def quicksort_lomuto_med(array, start, end, recursao, swaps):
    if(start < end):        
        recursao[0] +=1
        part_mediana3(array, start, end)        
        q = lomuto(array, start, end, swaps)        
        quicksort_lomuto_med(array,start, q - 1, recursao, swaps)    #Ordena os elementos antes do particionador atual       
        quicksort_lomuto_med(array, q + 1, end, recursao, swaps)     #Ordena os elementos depois do particionador atual

#Funcao Quicksort, utilizando o particionamento de Hoare random
def quicksort_hoare_rnd(array, start, end, recursao, swaps):
    if(start < end):
        recursao[0] +=1
        part_random(array, start, end)
        q = hoare(array, start, end, swaps)        
        quicksort_hoare_rnd(array,start, q, recursao, swaps)      #Ordena os elementos antes do particionador atual    
        quicksort_hoare_rnd(array, q + 1, end, recursao, swaps)       #Ordena os elementos depois do particionador atual

#Funcao Quicksort, utilizando o particionamento de Hoare mediana3
def quicksort_hoare_med(array, start, end, recursao, swaps):
    if(start < end):       
        recursao[0] +=1
        part_mediana3(array, start, end)        
        q = hoare(array, start, end, swaps)        
        quicksort_hoare_med(array,start, q, recursao, swaps)      #Ordena os elementos antes do particionador       
        quicksort_hoare_med(array, q + 1, end, recursao, swaps)       #Ordena os elementos depois do particionador

#Funcao do particionamento de Lomuto
def lomuto(array,start,end, swaps):      
    pivot = array[start] #particionador     
    i = start + 1 
    for j in range (start + 1,end + 1):                
        if array[j] <= pivot:
            swaps[0]+=1
            #Troca array[i] com array[j]
            aux = array[i]                 
            array[i] = array[j]
            array[j] = aux
            i = i + 1
            
    #Troca array[i + 1] com o particionador
    aux = array[i - 1]
    array[i - 1] = array[start]
    array[start] = aux        
    return(i - 1)    

#Funcao do particionamento de Hoare
def hoare(array,start,end, swaps):
    pivot = array[start]
    i = start - 1
    j = end + 1

    while True:
        i += 1
        while array[i] < pivot:
            i += 1        
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            swaps[0]+=1
            array[start], array[j] = array[j], array[start]    #colocar aqui para trocar            
            return j
        swaps[0]+=1
        array[i], array[j] = array[j], array[i]

def zera_o_bagulho(recursao, swaps):
    recursao[0]=0
    swaps[0]=0

def escrita(funcao,modo,texto):
    if(funcao == 'lomuto'):
        if(modo=='rnd'):
            arquivo = open('stats-aleatorio-lomuto.txt', 'w') 
        else:
            arquivo = open('stats-mediana-lomuto.txt', 'w')
    else:
        if(modo=='rnd'):
            arquivo = open('stats-aleatorio-hoare.txt', 'w') 
        else:
            arquivo = open('stats-mediana-hoare.txt', 'w')
        

    j = 0
    for i in texto:
        arquivo.write(texto[j])
        j=j+1
    arquivo.close()
    f.close()


def leitura_e_escrita(funcao,modo,tamanho):
    f = open('entrada-quicksort.txt','r') 
    textinho = []
    recursao = [0]
    swaps=[0]
    start = 0
    n = 0
    for i in tamanho:
        data = f.readline()
        #converte a string em uma lista de inteiros
        vet = [int(i) for i in data.split()]    
        #remove o primeiro valor, que era o tamanho
        del vet[0] 
        end = (len(vet) - 1)
        inicio = time.time() #variavel que ira cronometrar o tempo de execucao.
        textinho.append('TAMANHO ENTRADA ' + str(tamanho[n]))
        textinho.append('\n') 
        n += 1  
        if(funcao == 'lomuto'):
            if(modo == 'rnd'):
                quicksort_lomuto_rnd(vet, start, end, recursao, swaps)
            else:
                quicksort_lomuto_med(vet, start, end, recursao, swaps)
        else:
            if(modo == 'rnd'):
                quicksort_hoare_rnd(vet, start, end, recursao, swaps)
            else:
                quicksort_hoare_med(vet, start, end, recursao, swaps)
        #Calcula o tempo decorrido durante a execucao da funcao.
        fim = time.time()
        tempo = (fim - inicio)
        textinho.append('SWAPS ' + str(swaps[0])) 
        textinho.append('\n') 
        textinho.append('RECURSOES ' + str(recursao[0])) 
        textinho.append('\n')
        textinho.append('TEMPO ' + str(tempo))
        textinho.append('\n')
        #Zera as variaveis
        zera_o_bagulho(recursao,swaps)
    
    escrita(funcao,modo,textinho)
    
    


#Funcao main
#vai criar uma lista onde vai ser posto o texto antes de ser escrito no arquivo


##textinho = []
#recursao = [0]
#swaps=[0]
#start = 0
#n = 0

#abre o arquivo para criar uma lista com os tamanhos de cada array
with open('entrada-quicksort.txt','r') as f: 
    tamanho = [int(r.split()[0]) for r in f]

leitura_e_escrita('lomuto','rnd',tamanho)
leitura_e_escrita('lomuto','med',tamanho)
leitura_e_escrita('horae','rnd',tamanho)
leitura_e_escrita('horae','med',tamanho)
'''
#Abre o arquivo novamente. 
f = open('entrada-quicksort.txt','r') 
#pra cada linha ele armazena os valores numa string
for i in tamanho:
    data = f.readline()
    #converte a string em uma lista de inteiros
    vet = [int(i) for i in data.split()]    
    #remove o primeiro valor, que era o tamanho
    del vet[0] 
    end = (len(vet) - 1)
    inicio = time.time() #variavel que ira cronometrar o tempo de execucao.
    textinho.append('TAMANHO ENTRADA ' + str(tamanho[n]))
    textinho.append('\n') 
    n += 1  
    quicksort_lomuto_rnd(vet, start, end, recursao, swaps)
    #Calcula o tempo decorrido durante a execucao da funcao.
    fim = time.time()
    tempo = (fim - inicio)
    textinho.append('SWAPS ' + str(swaps[0])) 
    textinho.append('\n') 
    textinho.append('RECURSOES ' + str(recursao[0])) 
    textinho.append('\n')
    textinho.append('TEMPO ' + str(tempo))
    textinho.append('\n')
    #Zera as variaveis
    zera_o_bagulho(recursao,swaps)
    tempo = 0
    start = 0

#Cria o arquivo de saida.
arquivo = open('stats-aleatorio-lomuto.txt', 'w') 
j = 0
for i in textinho:
    arquivo.write(textinho[j])
    j=j+1
arquivo.close()
f.close()

#Zera as variaveis para ler o proximo arquivo
textinho = []
n = 0

#Abre o arquivo novamente. 
f = open('entrada-quicksort.txt','r') 
#pra cada linha ele armazena os valores numa string
for i in tamanho:
    data = f.readline()
    #converte a string em uma lista de inteiros
    vet = [int(i) for i in data.split()]    
    #remove o primeiro valor, que era o tamanho
    del vet[0] 
    end = (len(vet) - 1)
    inicio = time.time() #variavel que ira cronometrar o tempo de execucao.
    textinho.append('TAMANHO ENTRADA ' + str(tamanho[n]))
    textinho.append('\n') 
    n += 1  
    quicksort_lomuto_med(vet, start, end, recursao, swaps)
    #Calcula o tempo decorrido durante a execucao da funcao.
    fim = time.time()
    tempo = (fim - inicio)
    textinho.append('SWAPS ' + str(swaps[0])) 
    textinho.append('\n') 
    textinho.append('RECURSOES ' + str(recursao[0])) 
    textinho.append('\n')
    textinho.append('TEMPO ' + str(tempo))
    textinho.append('\n')
    #Zera as variaveis
    zera_o_bagulho(recursao,swaps)
    tempo = 0
    start = 0

#Cria o arquivo de saida.
arquivo = open('stats-mediana-lomuto.txt', 'w') 
j = 0
for i in textinho:
    arquivo.write(textinho[j])
    j=j+1
arquivo.close()
f.close()

#Zera as variaveis para ler o proximo arquivo
textinho = []
n = 0

#Abre o arquivo novamente. 
f = open('entrada-quicksort.txt','r') 
#pra cada linha ele armazena os valores numa string
for i in tamanho:
    data = f.readline()
    #converte a string em uma lista de inteiros
    vet = [int(i) for i in data.split()]    
    #remove o primeiro valor, que era o tamanho
    del vet[0] 
    end = (len(vet) - 1)
    inicio = time.time() #variavel que ira cronometrar o tempo de execucao.
    textinho.append('TAMANHO ENTRADA ' + str(tamanho[n]))
    textinho.append('\n') 
    n += 1  
    quicksort_hoare_rnd(vet, start, end, recursao, swaps)
    #Calcula o tempo decorrido durante a execucao da funcao.
    fim = time.time()
    tempo = (fim - inicio)
    textinho.append('SWAPS ' + str(swaps[0])) 
    textinho.append('\n') 
    textinho.append('RECURSOES ' + str(recursao[0])) 
    textinho.append('\n')
    textinho.append('TEMPO ' + str(tempo))
    textinho.append('\n')
    #Zera as variaveis
    zera_o_bagulho(recursao,swaps)
    tempo = 0
    start = 0

#Cria o arquivo de saida.
arquivo = open('stats-aleatorio-hoare.txt', 'w') 
j = 0
for i in textinho:
    arquivo.write(textinho[j])
    j=j+1
arquivo.close()
f.close()

#Zera as variaveis para ler o proximo arquivo
textinho = []
n = 0

#Abre o arquivo novamente. 
f = open('entrada-quicksort.txt','r') 
#pra cada linha ele armazena os valores numa string
for i in tamanho:
    data = f.readline()
    #converte a string em uma lista de inteiros
    vet = [int(i) for i in data.split()]    
    #remove o primeiro valor, que era o tamanho
    del vet[0] 
    end = (len(vet) - 1)
    inicio = time.time() #variavel que ira cronometrar o tempo de execucao.
    textinho.append('TAMANHO ENTRADA ' + str(tamanho[n]))
    textinho.append('\n') 
    n += 1  
    quicksort_hoare_med(vet, start, end, recursao, swaps)
    #Calcula o tempo decorrido durante a execucao da funcao.
    fim = time.time()
    tempo = (fim - inicio)
    textinho.append('SWAPS ' + str(swaps[0])) 
    textinho.append('\n') 
    textinho.append('RECURSOES ' + str(recursao[0])) 
    textinho.append('\n')
    textinho.append('TEMPO ' + str(tempo))
    textinho.append('\n')
    #Zera as variaveis
    zera_o_bagulho(recursao,swaps)
    tempo = 0
    start = 0

#Cria o arquivo de saida.
arquivo = open('stats-mediana-hoare.txt', 'w') 
j = 0
for i in textinho:
    arquivo.write(textinho[j])
    j=j+1
arquivo.close()
f.close()
'''