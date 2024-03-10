# i=input()
l=[]
for i in range(5):
    ele=input()
    l.append(ele)
s=sorted(l,reverse=True)# to sort the input list
m=min(s)#to find the minimum value 
print("the min value is" , m)
