buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('DATA BUAH')
for a,b in buah.items():
    print('-',a,'=',b)
print('Menu:')
print('A. Tambah data Buah')
print('B. Hapus data Buah')
print('C. Beli Buah')
print('D. Tutup Program')
while True:
    pilihan=input('Masukkan Pilihan Anda(A/B/C) = ')
    if (pilihan=='A'):
        while True:
            tambah=str(input('Masukkan nama buah yang ingin di data = '))
            if tambah in buah:
                print('Nama buah sudah ada')
                continue
            else:
                hargabaru=int(input('Masukkan harga buah='))
                buah.update({tambah:hargabaru})
                tambahlagi=str(input('Mau menambahkan lagi(y/n)?'))
                if (tambahlagi=='y'):
                    continue
                elif(tambahlagi=='n'):
                    print('DATA BUAH')
                    for a,b in buah.items():
                        print('-',a,'=',b)
                    break
        continue
    elif (pilihan=='B'):
        hapus=input('Masukkan data buah yang ingin dihapus = ')
        if hapus in buah:
            buah.pop(hapus)
            print('DATA BUAH')
            n=0
            for a,b in buah.items():
                n+=1
                print(n,'.',a,'=',b)
            continue
        else:
            print('Nama Buah Tidak Ditemukan')
            continue
    elif (pilihan=='C'):
        totalharga=0
        while True:
            namabuah=str(input('Nama buah yang akan dibeli = '))
            if namabuah in buah:
                jumlah=float(input('Berapa Kg                  = '))
                total=jumlah*buah[namabuah]
                totalharga+=total
                lagi=str(input('Mau beli buah yang lain(y/n)? '))
                if (lagi=='y'):
                    continue
                elif(lagi=='n'):
                    print('Total harga =Rp.',totalharga)
                    print('===================================================')
                    print('                   Terimakasih')
                    print('===================================================')

                    break
            else:
                print('Buah tidak tersedia')
                continue
    elif (pilihan=='D'):
        print('===================================================')
        print('                   Terimakasih')
        print('===================================================')

    break
