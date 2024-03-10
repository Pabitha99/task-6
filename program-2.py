def is_prime(i):
    count=0
    if i<=1:
        return False

    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            return False
    return True

def find_prime(inputs):
    count=0
    p=[]
    for i in inputs:
        if is_prime(i):
            p.append(i)
            count=count+1
    print("The total number of prime numbers:", count)
    return p
input=[10,501,22,37,100,999,87,351]
prime_num_list=find_prime(input)
print(f"The prime numbers are {prime_num_list}")


        




