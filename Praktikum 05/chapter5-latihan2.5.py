from random import randint
print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
bil=randint(0,10)
while True:
    jawaban=int(input('Tebakan Anda= '))
    if(jawaban > bil):
        print('Hehehe… Bilangan tebakan anda terlalu besar')
    elif(jawaban<bil):
        print('Hehehe… Bilangan tebakan anda terlalu kecil')
    elif(jawaban==bil):
        print('Yeeee… Bilangan tebakan anda BENAR :-)')
        break
