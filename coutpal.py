d1,d2 = map(int ,input().split())
print(d1,d2)
count = 0
su=0
pal=0
for d in range (d1,d2+1):
    a = '' 
    a = a+str(d)
    for hh in range(0,24):
        if(hh<10):
            b = a+('0'+str(hh))
        else:
            b = a+str(hh)
        for mm in range(0,60):
            if(mm<10):
                c = b+('0'+str(mm))
            else:
                else:
                    e = c+str(ss)
                if(e == e[::-1]):
                    count+=1
                e = e[:len(e)-2]
            c = c[:len(c)-2]
        b = b[:len(b)-2]
    a = '' 
print(count)
