Vo= int(input('Masukkan Kecepatan Mula-mula (Vo) = '))
Percepatan = int(input('Masukkan Percepatan (a) = '))
print('=================================================')
t=0
while(t<10):
    t+=1
    S= (Vo*t)+(Percepatan*t*t/2)
    print('t= ', t, ',', 'S(', t, ')=', S)
print('=================================================')
