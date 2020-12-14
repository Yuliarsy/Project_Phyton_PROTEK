#membuat function
def formasi1(n):
    for star in range (0,n):
        formasi = '*' *(1+(star-2)*2)
        print(formasi.center(1+2*n))
        
def formasi2(n):
    for star in range (0,n):
        formasi = '*' *(n+(star-1)*-2)
        print(formasi.center(1+2*n))
        
def formasi3(n):
        formasi1(n)
        formasi2(n)

while True:
    jumlah=int(input('Masukkan jumlah baris : '))
    if (jumlah%2==1):
        formasi3(jumlah)
        break
    else:
        print('Bilangan harus ganjil')
        lagi=input('masukkan lagi(y/n)? ')
        if(lagi=='y'): 
            continue
        else:
            break