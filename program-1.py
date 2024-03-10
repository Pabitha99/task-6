input=[10,501,22,37,100,999,87,351]
eve=[]#creating list for even
odd=[]#creating list for odd
for i in input:
    if i!=0 and i%2==0:
        eve.append(i)
    elif i!=0 and i%3==0:
        odd.append(i)
print(eve)
print(odd)







