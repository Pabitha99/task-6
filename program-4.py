i=int(input())
s=str(i)#converting integer to string, to iterate each values
first_num=int(s[0])#to get first num
last_num=int(s[-1])#to get last num
sums=first_num+last_num
print("the sum of first and last digit is ", sums)