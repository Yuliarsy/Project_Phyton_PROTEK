import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)
file = open(path + '/Data Karyawan.dat','r')
isiFile = file.readlines()

for i in range(len(isiFile)):
    isiFile[i] = isiFile[i].replace('\n','')
    isiFile[i] = isiFile[i].split('|')
    isiFile[i] = {'kode' : isiFile[i][0], 'nama' : isiFile[i][1], 'alamat' : isiFile[i][2], 'gol' : isiFile[i][3], 'tgl lahir' : isiFile[i][4], 'usia' : isiFile[i][5]}
    
j = 0
def Gaji():
    global gajiP
    if i.get('gol') == 'A':
        gajiP = 4000000
    if i.get('gol') == 'B':
        gajiP = 4500000
    if i.get('gol') == 'C':
        gajiP = 5000000
        
cari = input('Masukkan Kode Karyawan = ')
print('='*60)
for i in isiFile:
    if cari in i.values():
        print('Data Karyawan : \n')
        print('Kode             =', i.get('kode'))
        print('Nama             =', i.get('nama'))
        print('Alamat           =', i.get('alamat'))
        print('Golongan         =', i.get('gol'))
        print('Tanggal Lahir    =', i.get('tgl lahir'))
        Gaji()
        print('Gaji Pokok       =', gajiP )
        print('Usia             =', i.get('usia'))
        break
    else:
        j += 1
        if j == len(isiFile):
            print('Data Karyawan Tidak Ditemukan')
print('='*60)

file.close()