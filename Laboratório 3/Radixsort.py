#Laboratorio 3 CPD - Radix sort 
#Nomes: Luccas da Silva Lima e Bruno Longo Farina
#Turma: B

#Considere apenas as palavras contendo pelo menos 4 caracteres e apenas 
#letras do alfabeto ingles, isto e, ignore numerais e simbolos.


#variavel que vai armazenar o texto.
#O texto vai ser um vetor e cada palavra sera um nodo do vetor.
texto_completo = []
texto_real = []

#Essa funcao deleta do texto todas as palavras com menos de 4 letras
#e todas as strings que nao contem letras do alfabeto ingles
def deletext(texto):
    for i in range(0, len(texto)):
        if (len(texto[i]) >= 4):
            if(texto[i] >= 'A' and texto[i] <= 'Z'):
                texto_real.append(texto[i])

#Abre e le o arquivo inteiro.
with open('frankestein_clean.txt','r') as f: 
    data = f.readline()    
    texto = [str(i) for i in data.split()] 

#Chama a funcao para deletar todas as palavras com menos que 4 letras do texto.
deletest(texto)

#So criei um arquivo para testar se o vetor texto realmente tava com o texto certinho.
arquivo = open('escrita_teste.txt', 'w')
j = 0
i = 0
for i in texto_real:
    arquivo.write(texto_real[j])
    arquivo.write(' ')
    j=j+1
arquivo.close()