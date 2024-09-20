#Input
n1 = int(input("Enter the degree of the polynomial: "))
p1 = [0]*(n1+1)
for i in range(n1+1):
    a=int(input(f"Enter the coefficient of {i}th degree term: "))
    p1[i]=a

n2 = int(input("Enter the degree of the polynomial: "))
p2 = [0]*(n2+1)
for i in range(n2+1):
    a=int(input(f"Enter the coefficient of {i}th degree term: "))
    p2[i]=a


#Addition
def add(p1, p2):
    ret = p1.copy()
    min_length = min(len(p1), len(p2))
    for i in range(min_length):
        ret[i]+=p2[i]
    # if len(p1) > len(p2):
    #     ret.extend(p1[min_length:])
    if len(p1) < len(p2):
        ret.extend(p2[min_length:])
    return ret

#Multiply
def multiply(p1, p2):
    ret = [0]*(len(p1)+len(p2)+1)
    for i in range(0, len(p1)+1):
        for ind, val in enumerate(p2):
            ret[i+ind]+=p1[i]*val
    return ret

#Evaluate
def evaluate(p, x):
    ret = 0
    for ind, val in enumerate(p):
        ret+=val*(x**ind)
    return ret


print(add(p1, p2))
print(multiply(p1, p2))
