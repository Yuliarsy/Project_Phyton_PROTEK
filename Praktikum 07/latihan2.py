print('---------------------------------------------------------------------')
print('             PROGRAM UNTUK MENAMBAHKAN DATA PADA FILE')
print('---------------------------------------------------------------------')
namafile= input('Masukkan Nama File : ')
file= open(namafile,'a')
ulangi=True
while(ulangi==True):
    data= input('Masukkan data yang akan ditambahkan: ')
    file.write(data)
    pilihan= input('Ingin menambahkan lagi?(y/n): ')
    if(pilihan=='y'):
        ulangi=True
    elif(pilihan=='n'):
        ulangi=False
    else:
        print('Input yang anda masukkan Tidak Valid')
        break
file.close()
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
