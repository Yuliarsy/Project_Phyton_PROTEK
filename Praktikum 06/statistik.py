def sum(*n):
    i=0
    for b in n:
        i+=b
        hasil=i
    return hasil

def avg(*n):
    i=0
    for a in n:
        i+=1
        average=sum(*n)/i
    return average

def maks(*n):
    maksimum = n[0]
    for i in (n):
        if(i>maksimum):
            maksimum=i
    return maksimum 

def min(*n):
    minimum = n[0]
    for i in (n):
        if(i<minimum):
            minimum=i
    return minimum
