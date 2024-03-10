def is_happy_num(n):
    # str_i=str(i)
    sum=0
    visited=set()
    while n != 1 and n not in visited:
        visited.add(n)#to trace visited numbers
        # n = sum(int(digit) ** 2 for digit in str(n))# to get the sum of square of individual numbers
        for digit in str(n):
            a=int(digit) ** 2 
            sum=sum+a
    return n==1
            
def separate_happy_num(input_list):
    happy_num=[]
    non_happy_num=[]
    for n in input_list:
        if (is_happy_num(n)):
            happy_num.append(n)
        else:
            non_happy_num.append(n)
    return happy_num,non_happy_num

input_list=[10,501,22,37,100,999,87,351]
happy_nums, non_happy_nums= separate_happy_num(input_list)
print(happy_nums)
print(non_happy_nums)