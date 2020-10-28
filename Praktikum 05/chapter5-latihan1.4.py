KodeKaryawan=int(input('Masukan Kode Karyawan= '))
NamaKaryawan=str(input('Masukan Nama Karyawan= '))
Golongan=str(input('Masukan Golongan= '))
if(Golongan=='A'):
    GajiPokok= 10000000
    Potongan= 2.5
elif(Golongan=='B'):
    GajiPokok= 8500000
    Potongan= 2.0
elif(Golongan=='C'):
    GajiPokok= 7000000
    Potongan= 1.5
elif(Golongan=='D'):
    GajiPokok= 5500000
    Potongan= 1.0
else:
    print('GOLONGAN TIDAK DITEMUKAN,SILAHKAN INPUT ULANG')
    
TotalPotong = GajiPokok*(Potongan/100)
GajiBersih = GajiPokok-TotalPotong

print('===========================================')
print('        STRUK RINCIAN GAJI KARYAWAN        ')
print('===========================================')
print('Nama Karyawan   : ', NamaKaryawan)
print('Golongan        : ', Golongan)
print('-------------------------------------------')
print('Gaji Pokok      :Rp.', GajiPokok)
print('Potongan(',Potongan,'%):Rp.', TotalPotong)
print('-------------------------------------------')
print('Gaji Bersih     :Rp.', GajiBersih)
print('===========================================')
print('===========================================')
