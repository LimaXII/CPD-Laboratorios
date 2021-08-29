#Laboratorio 1 - CPD:
#Nomes: Luccas da Silva Lima e 
#Turma: B

#Sequencia a serem utilizadas:

#(Potencias de 2)
#SHELL = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,...]

#(Para numeros maiores que 701, os termos dessa sequencia sao gerados pela formula hk = 2.25h(index(k-1)).)
#KNUTH = [1,4,13,40,121,364,1093,3280,9841,29524,88573,265720,797161,2391484,...]

#CIURA = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711,....] 

#Shell_sort. Recebe como parametro um vetor e o seu tamanho.
def shell_sort(array,n,seq): 
    #define o meio do array.
    meio = n // 2
    #inicia i valendo 0 e percorre o vetor da sequencia utilizada (shell, knuth ou ciura)
    i = 0
    while i < 20:
        #caso ache um valor em seq[i+1] MAIOR que a posicao presente no meio do vetor, utiliza seq[i]
        if seq[i+1] > meio:    
            #enquanto i, variavel que ira percorrer o vetor das sequencias, for maior ou igual a 0:                    
            while i >= 0: 
                #com j comecando em seq[i] e indo ate o numero de elementos do vetor a ser ordenado               
                for j in range(seq[i], n):  
                    #variavel auxiliar recebe o valor do vetor a ser ordenado na posicao j. array[j]                  
                    aux = array[j]
                    #contador_aux recebe o valor de j
                    contador_aux = j                    
                    while contador_aux >= seq[i] and array[contador_aux - seq[i]] > aux:
                        #TROCA o numero na posicao contador_aux do vetor a ser ordenado, pelo conteudo na posicao array[x - incremento].
                        array[contador_aux] = array[contador_aux - seq[i]]
                        #contador_aux recebe a posicao que foi utilizada acima: array[x - incremento]                        
                        contador_aux = contador_aux - seq[i]
                    #Troca o outro valor do vetor. array[contador_aux]:
                    array[contador_aux] = aux
                    #Como as 'trocas' sao realizadas utilizando variaveis auxiliares, cada uma delas deve ser feita separadamente.
                #printa o array, informando qual incremento foi utilizado.
                print(array, 'INCR =',seq[i])
                #decrementa i, para retroceder uma posicao no vetor das sequencias.                
                i = i - 1
            #Caso o ordenamento tenha acontecido, i = 20 para interromper o loop no while.
            i = 20
        #Caso seq[i+1] nao for > meio, incrementa i.
        else:
            i = i + 1
              
                      

#Sequencias utilizadas:
shell = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
knuth = [1,4,13,40,121,364,1093,3280,9841,29524,88573,265720,797161,2391484]
ciura = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711] 

#Primeiro vetor do arquivo entrada1.txt:
array = [8, 2, 10, 11, 3, 9, 9, 15, 4, 14, 9, 6, 13, 3, 4, 8,]
#n = array length
n = len(array)

#Printa informacoes na tela e chama a funcao shell_sort
print(array, 'SEQ = SHELL')
shell_sort(array,n,shell)
print()
array = [8, 2, 10, 11, 3, 9, 9, 15, 4, 14, 9, 6, 13, 3, 4, 8,]
print(array, 'SEQ = KNUTH')
shell_sort(array,n,knuth)
print()
array = [8, 2, 10, 11, 3, 9, 9, 15, 4, 14, 9, 6, 13, 3, 4, 8,]
print(array, 'SEQ = CIURA')
shell_sort(array,n,ciura)
print()