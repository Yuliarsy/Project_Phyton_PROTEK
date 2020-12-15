#membuat function
def bintang(n):
    for star in range (1,n):
        formasi = '*' *(1+(star-1)*2)
        print(formasi.center(1+2*n))
        
bintang(5)