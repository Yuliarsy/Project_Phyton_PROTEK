import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)

openfile = open(path + '/enkripsiCaesar.txt','r')
dekripsi= openfile.readline()
buatlist = list(dekripsi) 

n = int(input('Masukkan jumlah pergeseran = '))

dekripsisandicaesar = ''
for huruf in buatlist:
    if (huruf.isalpha()):
        ascii= ord(huruf)
        caesar = 65 + ((ascii % 65)- n)%26
        dekripsisandicaesar += chr(caesar)
    else : 
        dekripsisandicaesar += ' '
print('Hasil enkripsi             = ', dekripsisandicaesar)
print('*hasil enkripsi disimpan dalam file', 'dekripsiCaesar.txt')
openfile = open(path + '/dekripsiCaesar.txt','w')
openfile.write(dekripsisandicaesar)
openfile.close