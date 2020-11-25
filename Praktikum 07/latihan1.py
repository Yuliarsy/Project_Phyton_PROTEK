try:
    namafile= input('Masukkan Nama File:')
    print('isi dari file',namafile,':')
    file=open(namafile,'r')
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')
