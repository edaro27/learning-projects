
people=[ 50,100]
count=dict()

for i,item in enumerate(people):
    count[item]=count.get(item,0)+1
    if item==50:
        if count.get(25)>=1:
            if (i+1)==len(people):
                print "YES"
                break
            count[25]=count[25]-1
            continue
        else: 
            print "NO"
            break
    if item==100:
        if count.get(25)>=1 and count.get(50)>=1:
            if (i+1)==len(people):
                print "YES"
                break
            count[25]=count[25]-1
            count[50]=count[50]-1
            continue
        if  count.get(25)>=3:
            if (i+1)==len(people):
                print "YES"
                break
            count[25]=count[25]-3
            continue 
        else: 
            print "NO"
            break
    if item==25:
        if (i+1)==len(people):
            print "YES"
            break
        continue  
        