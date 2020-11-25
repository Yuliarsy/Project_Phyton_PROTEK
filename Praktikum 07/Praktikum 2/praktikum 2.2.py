try:
    file = open('d:\ProjectPhyton\Project_Phyton_PROTEK\Praktikum 07\Praktikum 2\data.txt','r')
    bil1 = int(file.readline())
    bil2 = int(file.readline())
    hasil= bil1/bil2
    print(bil1,'dibagi',bil2,'sama dengan',hasil)
except FileNotFoundError:
    print('File tidak ditemukan')
except ZeroDivisionError:
    print('Tidak dapat dibagi dengan nol')
