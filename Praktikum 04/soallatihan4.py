
import math
#KeteranganSoal
JarakkotaAkeB= 125
JarakkotaBkeC= 256
KecepatantempuhAB= 62
KecepatantempuhBC= 70
JamBerangkat= 6
WaktuIstirahat= 45

#KecepatanperMenit
KecepatantempuhABperMenit= (KecepatantempuhAB/60)
KecepatantempuhBCperMenit= (KecepatantempuhBC/60)

#WaktuTempuh
WaktuTempuhAB= math.ceil(JarakkotaAkeB/KecepatantempuhABperMenit)
WaktuTempuhBC= math.ceil(JarakkotaBkeC/KecepatantempuhBCperMenit)

#JumlahWaktuTempuh
WaktuTempuhKeseluruhan= (WaktuTempuhAB+WaktuIstirahat+WaktuTempuhBC)
WaktudalamJam=(WaktuTempuhKeseluruhan//60)+JamBerangkat
JumlahMenitTempuh= WaktuTempuhKeseluruhan%60

print("Pak Amir sampai di Kota C pada pukul",(WaktudalamJam)," ",(MenitTempuh))
