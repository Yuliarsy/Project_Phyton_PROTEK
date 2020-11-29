def ratarata(a):
    ubah= tuple(a.values())
    jumlahseluruh= sum(ubah)
    jumlahbil= len(ubah)
    rata= jumlahseluruh/jumlahbil
    return rata

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('Rata-rata harga satuan nya adalah' ,ratarata(buah))
