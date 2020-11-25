print('---------------------------------------------------------------------')
print('                 PROGRAM UNTUK MENGHITUNG RATA RATA')
print('---------------------------------------------------------------------')
bilangan= True
jumlah=0
jumlahbilangan=0
while(bilangan==True):
    try:
        inputbilangan= int(input('Masukkan Bilangan Bulat : '))
        jumlah+=inputbilangan
        jumlahbilangan+=1
        pilihan= input('Ingin memasukkan bilangan lagi?(y/n): ')
        if(pilihan=='y'):
            bilangan=True
        elif(pilihan=='n'):
            bilangan=False
        else:
            print('Input yang anda masukkan Tidak Valid')
    except ValueError:
        print('Yang anda masukkan bukan bilangan bulat')
        continue
print('---------------------------------------------------------------------')
rata=jumlah/jumlahbilangan
print('Rata-Ratanya adalah     :',rata)
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
