from random import randint
JumlahPerulangan=0
while True:
    bil= randint(0,10)
    print(bil)
    JumlahPerulangan+=1
    if bil== 5:
        break
print('Jumlah Perulangan= ',JumlahPerulangan)
