import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)

text = 'SAYA SUKA PYTHON'
buatlist = list(text)
print('Program Enkripsi Sandi Caesar')
print(text)
n = int(input('Masukkan jumlah pergeseran = '))

sandicaesar = ''
for huruf in buatlist:
    if (huruf.isalpha()):
        ascii= ord(huruf)
        caesar = 65 + ((ascii % 65)+ n)%26
        sandicaesar += chr(caesar)
    else : 
        sandicaesar += ' '
print('Hasil enkripsi             = ', sandicaesar)
print('*hasil enkripsi disimpan dalam file', 'enkripsiCaesar.txt')
openfile = open(path + '/enkripsiCaesar.txt','w')
openfile.write(sandicaesar)
openfile.close