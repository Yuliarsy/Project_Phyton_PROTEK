import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)
openfile = open(path + '/bilangan.txt','r')
databaru = ''
bil1=[]
bil2=[]
n=0
for bilangan in openfile:
    splitbilangan= bilangan.split('|')
    jumlah = int(splitbilangan[0]) + int(splitbilangan[1].strip())
    databaru += str(jumlah)+ '\n'

openfile = open(path + '/hasiljumlah.txt','w')
openfile.write(databaru)
openfile.close