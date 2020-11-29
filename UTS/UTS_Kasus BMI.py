print('PROGRAM PERHITUNGAN STATUS BERAT BADAN')
print('========================================')
#Input
BeratBadan=int(input('Masukkan Berat Badan (Kg) = '))
TinggiBadan1=int(input('Masukkan Tinggi Badan (Cm)= '))

#Perhitungan BMI
TinggiBadan2=TinggiBadan1/100
BMI=BeratBadan/(TinggiBadan2*TinggiBadan2)

#Status Berat Badan
print('Status Berat Badan : ', end='')
if(BMI<18):
    print('KURUS')
elif(18<=BMI<23):
     print('IDEAL')
elif(23<=BMI<27):
     print('GEMUK')
elif(27<=BMI<35):
     print('OBESITAS')
else:
    print('OBESITAS MORBID')
print('========================================')
