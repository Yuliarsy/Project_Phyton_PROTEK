x= int(input('Jumlah bilangan yang ingin dimasukkan = '))
a=[]
i=0
for i in range (x):
    ab = int(input('Masukkan Bilangan = '))
    a.append(ab)
a.sort()
a.reverse()
print('list =', a)
