import pathlib
from datetime import datetime

path = current_dir = str(pathlib.Path(__file__).parent)

skg = datetime.now()
tahun = skg.year

def getUsia(tgl):
    global usia
    usia = tahun - int(tgl[:4])
    print('Usia : ', usia, 'tahun')
    
def init(nip,nama,alamat,gol,tgl):
    output = open(path + '/Data Karyawan.dat','a')
    data = nip + '|' + nama + '|' + alamat + '|' + gol + '|' + tgl + '|' + str(usia) + '\n'
    output.write(data)
    output.close()

while True:
    nip = input('Masukkan NIP\t: ')
    nama = input('Masukkan Nama\t: ')
    alamat = input('Masukkan Alamat\t: ')
    gol = input('Masukkan Golongan (A/B/C)\t: ')
    tgl = input('Masukkan Tgl Lahir (YYYY-MM-DD)\t: ')
    getUsia(tgl)
    init(nip,nama,alamat,gol,tgl)
    
    tambahdata = input('Tambah data (y/n) :')
    if tambahdata == 'y':
        continue
    else:
        break
    
output = open(path + '/Data Karyawan.dat','r')
print(output.read())
output.close()