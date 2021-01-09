import datetime
 

def diffDate(x):
    sekarang=datetime.date.today()
    listtanggal= x.split('-')
    yyyy  = int(listtanggal[0])
    mm = int(listtanggal[1])
    dd = int(listtanggal[2])

    selisih= sekarang- datetime.date(yyyy,mm,dd)
    return abs(selisih.days)

print(diffDate(2021-1-1))