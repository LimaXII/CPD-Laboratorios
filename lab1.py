#Laboratorio 1 - CPD:
#Nomes: Luccas da Silva Lima e Bruno Longo Farina
#Turma: B

import time #biblioteca necessaria para cronometrar o tempo.

#vai criar uma lista onde vai ser posto o texto antes de ser escrito no arquivo
textinho = []
#mesma ideia da outra variavel
textinho2 = []

#funcao que define qual sequencia devera ser utilizada.
def definir_seq(seq):
    if seq[2] == 4:
        return 'SHELL'
    elif seq[2] == 13:
        return 'KNUTH'
    else:
        return 'CIURA'

#Funcao shell_sort. Recebe como parametro um vetor, o seu tamanho e uma sequencia.
def shell_sort(array,n,seq):   
    
    #exercicio 1:
    #escreve no textinho o array intacto e qual sequencia está sendo utilizada (ver se n é melhor fazer isso dentro da main ao inves da função)
    textinho.append(str(array))
    textinho.append('SEQ = ')
    textinho.append(definir_seq(seq))#aqui ta dando problema, ele tá escrevendo os números da sequencia ao invés de 
    textinho.append('\n')

    #exercicio 2:
    #!!! Talvez tentar colcoar isso na main ou em outra funcao, nao sei qual seria a melhor escolha.
    #O programa funciona perfeitamente desse jeito, so fica meio baguncado 
    if n >= 100:
        inicio = time.time() #variavel que ira cronometrar o tempo de execucao.    
        textinho2.append(definir_seq(seq))
        textinho2.append(', ')    
        textinho2.append(str(n))
        textinho2.append(', ')

    #inicia i valendo 0 e percorre o vetor da sequencia utilizada (shell, knuth ou ciura)
    i = 0
    while i < 20:
        #caso ache um valor em seq[i+1] MAIOR que a posicao presente no meio do vetor, utiliza seq[i]
        if seq[i+1] >= n:    
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
                #!!! Talvez remover esse print ajude no desempenho do algoritmo.
                print(array, 'INCR =',seq[i])

                #vai colocar numa lista essa string que acabou de ser disposta
                textinho.append(str(array))
                textinho.append('INCR =')
                textinho.append(str(seq[i]))
                textinho.append('\n')
                #decrementa i, para retroceder uma posicao no vetor das sequencias.                
                i = i - 1
            #Caso o ordenamento tenha acontecido, i = 20 para interromper o loop no while.
            i = 20
            
            #!!! Talvez tentar colcoar isso na main ou em outra funcao, nao sei qual seria a melhor escolha.
            #O programa funciona perfeitamente desse jeito, so fica meio baguncado            
            if n >= 100:
                fim = time.time()
                tempo = (fim - inicio)
                textinho2.append(str(tempo))
                textinho2.append('\n')    

        #Caso seq[i+1] nao for >= n, incrementa i.
        else:
            i = i + 1
    
              
                      

#Sequencias utilizadas:
shell = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
knuth = [1,4,13,40,121,364,1093,3280,9841,29524,88573,265720,797161,2391484]
ciura = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711] 

#Exercicio 1:
#abre o arquivo para criar uma lista com os tamanhos de cada array
with open('entrada1.txt','r') as f: #C:\\Users\\bruno\\OneDrive\\Documentos\\GitHub\\Lab1-Shell_sort\\
    tamanho = [int(r.split()[0]) for r in f]

#abre o arquivo de novo (n sei pq fechou)
f = open('entrada1.txt','r') #C:\\Users\\bruno\\OneDrive\\Documentos\\GitHub\\Lab1-Shell_sort\\

#pra cada linha ele armazena os valores numa string
for i in tamanho:
    data = f.readline()
    #converte a string em uma lista de inteiros
    res = [int(i) for i in data.split()]
    #remove o primeiro valor, que era o tamanho 
    del res[0]    
    #e faz o shell sort dela
    shell_sort(res,i,shell)
    shell_sort(res,i,knuth)
    shell_sort(res,i,ciura)
   
    #arquivo.write(str(res)+'\n')
arquivo = open('saida1.txt', 'w') #C:\\Users\\bruno\\OneDrive\\Documentos\\GitHub\\Lab1-Shell_sort\\
j = 0
for i in textinho:
    arquivo.write(textinho[j])
    j=j+1
arquivo.close()
f.close()

#Exercicio 2:
tamanho = [100, 1000, 10000, 100000, 1000000]
f = open('entrada2.txt', 'r') 
for i in tamanho:
    data = f.readline()
    #converte a string em uma lista de inteiros
    res = [int(i) for i in data.split()]
    #remove o primeiro valor, que era o tamanho 
    del res[0]    
    #e faz o shell sort dela
    shell_sort(res,i,shell)    
    shell_sort(res,i,knuth)
    shell_sort(res,i,ciura)

arquivo = open('saida2.txt', 'w') 
j = 0
for i in textinho2:
    arquivo.write(textinho2[j])
    j=j+1
arquivo.close()
f.close()
