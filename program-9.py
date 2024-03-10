def find_triplet(l,target):#giving arguments list and targeted sum value
    result=[]
    l.sort()#sorting the list
    for i in range(len(l)-2):
        left=i+1
        right=len(l)-1
        while left < right:
            current_sum=l[i]+l[left]+l[right]
            if current_sum==target:
                result.append((l[i],l[left],l[right]))
                left=left+1
                right=right-1
            elif current_sum<target:
                left=left+1
            else:
                right=right-1
    return result   

#input
l=[10,20,30,9]
s=len(l)
target=59
# sum=8
total_sum=find_triplet(l,target)
print("The triplets are", total_sum)