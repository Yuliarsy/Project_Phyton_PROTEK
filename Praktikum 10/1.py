import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)

openfile = open(path + '/text.txt','r')

ganjil = 0
genap = 0 

for nilai in openfile:
    if(int(nilai)%2 == 0):
        genap +=1
    elif(int(nilai)%2 == 1) :
        ganjil+=1

print('Banyak bilangan ganjil =', ganjil)
print('Banyak bilangan genap =', genap)
