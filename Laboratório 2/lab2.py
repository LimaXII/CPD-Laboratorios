#Laboratorio 2 CPD - Quicksort 
#Nomes: Luccas da Silva Lima e Bruno Longo Farina
#Turma: B

#Biblioteca que gera numeros aleatorios
import random
import statistics

#Funcao que seleciona a mediana entre 3 valores presentes no vetor (Valor inicial, final, e meio)
#Sinceramente ficou uma gambiarra bem grande, mas nsei como arrumar mto bem ainda
#Pode mudar se quiser
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
def quicksort_lomuto_rnd(array, start, end):
    if(start < end):
        part_random(array, start, end)
        q = lomuto(array, start, end)     
        quicksort_lomuto_rnd(array,start, q - 1)     #Ordena os elementos antes do particionador atual       
        quicksort_lomuto_rnd(array,q + 1, end)       #Ordena os elementos depois do particionador atual

#Funcao Quicksort, utilizando o particionamento de Lomuto
def quicksort_lomuto_med(array, start, end):
    if(start < end):        
        part_mediana3(array, start, end)        
        q = lomuto(array, start, end)        
        quicksort_lomuto_med(array,start, q - 1)     #Ordena os elementos antes do particionador atual       
        quicksort_lomuto_med(array, q + 1, end)      #Ordena os elementos depois do particionador atual

#Funcao Quicksort, utilizando o particionamento de Hoare random
def quicksort_hoare_rnd(array, start, end):
    if(start < end):
        part_random(array, start, end)
        q = hoare(array, start, end)        
        quicksort_hoare_rnd(array,start, q - 1)      #Ordena os elementos antes do particionador atual    
        quicksort_hoare_rnd(array, q + 1, end)       #Ordena os elementos depois do particionador atual

#Funcao Quicksort, utilizando o particionamento de Hoare mediana3
def quicksort_hoare_med(array, start, end):
    if(start < end):
        part_mediana3(array, start, end)
        q = hoare(array, start, end)        
        quicksort_hoare_med(array,start, q - 1)      #Ordena os elementos antes do particionador       
        quicksort_hoare_med(array, q + 1, end)       #Ordena os elementos depois do particionador

#Funcao do particionamento de Lomuto
def lomuto(array,start,end):      
    x = array[start] #particionador     
    i = start + 1 
    for j in range (start + 1,end + 1):                
        if array[j] <= x:
            
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
def hoare(array,start,end):
    pivot = array[start]
    i = start + 1
    j = end

    while True:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            array[start], array[j] = array[j], array[start]    #colocar aqui para trocar
            return j
        array[i], array[j] = array[j], array[i]

    


#Funcao main
teste = [19,5,2,10,9,25,93,52,33,2,9,41,8]  #Sequencia de teste
start = 0
end = (len(teste) - 1)


#Chama a funcao quicksort, utilizando lomuto e random
quicksort_lomuto_rnd(teste, start, end)
print("Array pos ordenamento (Lomuto random): ", teste)
teste = [19,5,2,10,9,25,93,52,33,2,9,41,8]  #Sequencia de teste

quicksort_hoare_med(teste, start, end)
print("Array pos ordenamento (horae medio): ", teste)

#Chama a funcao quicksort, utilizando lomuto e med3
#teste = [19,5,2,10,9,25,93,41,8]  #Reseta a sequencia de teste
#quicksort_lomuto_med(teste, start, end)
#print("Array pos ordenamento (Lomuto med3): ", teste)