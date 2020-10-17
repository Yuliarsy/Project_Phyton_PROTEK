import math

#Keterangan soal
JarakkotaAkeC= 795
Jaraktempuhyangdiapaidengan1liter= 12

#Menghitung Bensin yang diperlukan
Bensinyangdiperlukan= JarakkotaAkeC/Jaraktempuhyangdiapaidengan1liter

#Menghitung Jumlah Pengisian yang harus dilakukan
IsiTangkiBensinsaatBerangkat= 50
JumlahPengisian= math.floor(Bensinyangdiperlukan/IsiTangkiBensinsaatBerangkat)

print ("Jumlah pengisian yang harus dilakukan pak budi untuk mencapai kota C=",JumlahPengisian, "kali")
