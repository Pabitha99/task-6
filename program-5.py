def distribute_mango(mango_bags,num_students):
    s=sorted(mango_bags)
    sorted_bag=[]
    min_diff=float('inf')#unbounded positive value
    left=0
    right=num_students-1
    while right<len(s):
        current_diff=s[right]-s[left]
        if current_diff<min_diff:
            min_diff=current_diff
            sorted_bag=s[left:right+1]
        left+=1
        right+=1
    return sorted_bag

# inputs
mango_bags = [7, 3, 10, 8, 12, 5]
num_students = 3
selected_bags=distribute_mango(mango_bags,num_students)
print(selected_bags)