#Status Kelulusan Mahasiswa
print("Cek Status Kelulusan Mahasiswa")
nilaiBahasaIndonesia= int(input("Masukan Nilai Bahasa Indonesia= "))
nilaiIPA= int(input("Masukan Nilai IPA= "))
nilaiMatematika= int(input("Masukan Nilai Matematika="))
print("_____________________________________")
print("Status Kelulusan Mahasiswa= ",end='')

if(nilaiBahasaIndonesia>60 and nilaiIPA>60 and nilaiMatematika>70):
                      print("LULUS")
else:
    print("TIDAK LULUS")
    
