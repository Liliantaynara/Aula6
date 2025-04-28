a = [""]*5
m = [""]*5

for j in range ( len(a)):
   a[j]= int(input (f"digite um valor:" ))
x=  int(input("digite valor: "))

for i in range (len(m)):
    m[i]= x*a [i]

print (a)
print (x)
print (m)
