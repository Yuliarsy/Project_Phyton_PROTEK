try:
    file = open('d:/ProjectPhyton/Project_Phyton_PROTEK/Praktikum 07/Praktikum 3/data.txt','r')
    sum = 0
    for data in file:
        sum = sum + int(data)
    print(sum)
except ValueError:
    print('Tipe data tidak valid')
