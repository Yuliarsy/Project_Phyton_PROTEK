#list
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
#program
print('===================================================')
print('                   TOKO BUAH')
print('===================================================')
namabuah=str(input('Nama buah yang akan dibeli = '))
a= namabuah in buah
r=True
if a:
    while (r==True):
        jumlah=float(input('Berapa Kg                  = '))
        harga= buah.get(namabuah,0)
        Total=jumlah*harga
        print('===================================================')
        print('Total                      = Rp.',Total)
        break
else:
    print('Buah tidak tersedia')
