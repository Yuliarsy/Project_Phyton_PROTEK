import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)
data = ''
while True: 
    openfile = open(path + '/input biodata.txt','a')
    NIM = input('Masukkan NIM :')
    Nama =input('Masukkan Nama :')
    Alamat =input('Masukkan Alamat :')
    formatdata= NIM + '|' + Nama + '|' + Alamat + '\n'
    Ulangi =input('Ingin Memasukkan data lagi? y/n :')
    if (Ulangi=='y'):
        openfile.write(formatdata)
        openfile.close
        continue
    elif (Ulangi=='n'):
        openfile.write(formatdata)
        openfile.close
        break