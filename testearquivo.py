

with open('entrada2.txt', 'r') as f:
    tamanho = [int(r.split()[0]) for r in f]      

with open('entrada2.txt', 'r') as f:    
    data = f.readline()
res = [int(i) for i in data.split()]

print(res)
print()
print(tamanho)