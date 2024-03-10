number=[4,2,-3,1,6]
# number=list(map(int,input().split()))
# print(number)
sub_set=[]
value=0
for i in range(0,(len(number)+1)):
    for j in range(i+1,(len(number)+1)):
        sub_set.append(number[i:j])
        # print(sub_set)
for i in sub_set:
    if sum(i)==0:
        print(i)
        value=1
if(value==1):
    print("It is sub-list with sum=0")
else:
    print("It is not having sub-list with sum=0")
