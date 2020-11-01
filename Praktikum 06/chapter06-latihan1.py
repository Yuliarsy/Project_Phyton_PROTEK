def isPhytagoras (a,b,c):
    if(a*a+b*b==c*c):
        print('a=', a, 'b=',b,'c=',c, '-> TRUE')
    else:
        print('a=',a,'b=',b,'c=',c, '-> FALSE')
        
isPhytagoras(3,4,5)
isPhytagoras(5,9,12)
isPhytagoras(8,6,10)
isPhytagoras(7,8,11)
