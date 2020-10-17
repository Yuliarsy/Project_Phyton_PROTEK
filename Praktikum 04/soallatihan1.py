import math
#Tarif Rental
TarifRental1= 200000
TarifRental2= 10000

#Keterangan Jam
JamMulaiSewa= 6
MenitMulaiSewa= 0
JamSelesaiSewa= 23
MenitSelesaiSewa= 50

#Menghitung Lama Sewa
LamaSewa= math.floor((JamSelesaiSewa-JamMulaiSewa) + MenitSelesaiSewa/60)

#Menghitung Tarif Sewa
TarifSewa= TarifRental1+(TarifRental2*(LamaSewa-12))

print ("Tarif yang harus dibayarkan=", TarifSewa)
