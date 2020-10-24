#Status Kelulusan Mahasiswa
print("Cek Status Kelulusan Mahasiswa")
nilaiBahasaIndonesia= int(input("Masukan Nilai Bahasa Indonesia= "))
nilaiIPA= int(input("Masukan Nilai IPA= "))
nilaiMatematika= int(input("Masukan Nilai Matematika="))
print("_____________________________________")
print("Status Kelulusan Mahasiswa= ",end='')

if(nilaiBahasaIndonesia<0 or nilaiBahasaIndonesia>100):
    print("Maaf input ada yang tidak valid")
elif(nilaiIPA<0 or nilaiIPA>100):
    print("Maaf input ada yang tidak valid")
elif(nilaiMatematika<0 or nilaiMatematika>100):
    print("Maaf input ada yang tidak valid")
elif(nilaiBahasaIndonesia>60 and nilaiIPA>60 and nilaiMatematika>70):
                      print("LULUS")
else:
    print("TIDAK LULUS")
    print("Sebab Tidak Lulus=")
    if(nilaiBahasaIndonesia<60):
        print("Nilai Bahasa Indonesia kurang dari 60")
    if(nilaiIPA<60):
        print("Nilai IPA kurang dari 60")
    if(nilaiMatematika<70):
        print("Nilai Matematika kurang dari 70")
