a=[1,3,1,2,4]#input
count=0
for i in a:
    if a.count(i)==1:#to check non_repeatable vale
        print (i)
        count=count+1
        if count>=1:
            continue