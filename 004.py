n1 = []*5
soma = 0
cont = 0

for c in range (len(n1)):
    n1[c]= float(input("digite a nota: "))

for t in range (len(n1)):
    soma+=n1[t]
media=soma/(len(n1))

for j in range(len(n1)):
    if n1 [j]>media:
        cont+=1
    print (cont)