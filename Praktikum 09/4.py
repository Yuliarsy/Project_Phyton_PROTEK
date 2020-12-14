import random
def shuffleString(kata,jumlah):
     buatlist = []
     i = 0
     while i<jumlah:
        acak=[''.join(random.sample(kata,len(kata)))]
        if(acak not in buatlist):
            buatlist += acak
            i+=1
     print(buatlist)

shuffleString('aku',2)
shuffleString('aku',3)
shuffleString('aku',4)
