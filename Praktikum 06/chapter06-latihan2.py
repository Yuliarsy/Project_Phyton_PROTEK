#kotak bintang ajaib
def StarFormation1():
    kolom = 0
    baris = 5

    i=0
    while (i<baris):
        j=0
        while (j<=kolom):
            print('*', end='')
            j+=1
        print('')
        i+=1
        kolom +=1
    
def StarFormation2():
    kolom = 4
    baris = 5

    i=0
    while (i<=baris):
        j=0
        while (j<kolom):
            print('*', end='')
            j+=1
        print('')
        i+=1
        kolom -=1

StarFormation1()
StarFormation2()
