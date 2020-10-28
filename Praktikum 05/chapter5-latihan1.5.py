KodeKaryawan=int(input('Masukan Kode Karyawan= '))
NamaKaryawan=str(input('Masukan Nama Karyawan= '))
Golongan=str(input('Masukan Golongan= '))
Status=int(input('Masukan Status(1(Menikah),2(Belum Menikah)='))
if(Status==1):
    JumlahAnak=int(input('Masukan Jumlah Anak='))
    
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
if(Status==1):
    tunjangan= GajiPokok*(10/100)
    tunjanganAnak= GajiPokok*(5/100)*JumlahAnak
    GajiKotor= GajiPokok+tunjangan+tunjanganAnak
    GajiBersih= GajiKotor-TotalPotong
GajiBersih2=GajiPokok-TotalPotong
print('===========================================')
print('        STRUK RINCIAN GAJI KARYAWAN        ')
print('===========================================')
print('Nama Karyawan         : ', NamaKaryawan)
print('Golongan              : ', Golongan)
print('Status                :  ', end='')
if(Status==1):
    print('Menikah')
else:
    print('Belum Menikah')
if(Status==1):
    print('Jumlah Anak           : ', JumlahAnak)
print('-------------------------------------------')
print('Gaji Pokok            :Rp.', GajiPokok)
if(Status==1):
    print('Tunjangan Istri/Suami :Rp.', tunjangan)
    print('Tujangan Anak         :Rp.', tunjanganAnak)
    print('----------------------------------------- +')
    print('Gaji Kotor            :Rp.', GajiKotor)
print('Potongan(',Potongan,'%)      :Rp.', TotalPotong)
print('----------------------------------------- -')
if(Status==1):
    print('Gaji Bersih           :Rp.',GajiBersih)
else:
    print('Gaji Bersih           :Rp.',GajiBersih2)
print('===========================================')
print('===========================================')

