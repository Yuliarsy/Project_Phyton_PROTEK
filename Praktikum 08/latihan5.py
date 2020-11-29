def kuadrat(bil):
    l=[]
    for i in range (len(bil)):
        bil[i]**=2
    return bil

n= int(input('Jumlah bilangan yang ingin dimasukkan = '))
bil=[]
for i in range (n):
    ab = int(input('Masukkan Bilangan = '))
    bil.append(ab)
print(kuadrat(bil))
