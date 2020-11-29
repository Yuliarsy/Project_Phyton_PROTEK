def dataStat(x):
    r=[]
    a= sum(x)/len(x)
    b= max(x)
    c= min(x)
    r.extend([a,b,c])
    return(a,b,c)
#Menginputkan List
n= int(input('Jumlah bilangan yang ingin dimasukkan = '))
a=[]
i=0
for i in range (n):
    ab = int(input('Masukkan Bilangan = '))
    a.append(ab)
print(dataStat(a))

