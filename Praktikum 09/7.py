mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print('='*65)
print('NIM'.ljust(7),'NAMA MAHASISWA'.ljust(22),'TANGGAL LAHIR'.ljust(17),'TEMPAT LAHIR')
print('-'*65)
for isi in mhs:
    isiSplit = isi.split(':')
    NIM = isiSplit[0]
    Nama = isiSplit[1]
    TanggalLahir = isiSplit[2]
    TanggallahirSplit=TanggalLahir.split('-')
    Tanggal=TanggallahirSplit[2]
    Bulan=TanggallahirSplit[1]
    Tahun=TanggallahirSplit[0]
    TempatLahir=isiSplit[3]
    print(NIM.ljust(7),Nama.ljust(22),Tanggal,'/',Bulan,'/', Tahun.ljust(7),TempatLahir)
print('='*65)