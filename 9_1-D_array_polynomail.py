def take_input():
    n=int(input("Enter highest degee of polynomial :"))
    poly = []
    for i in range(n+1):
        x=int(input("Enter coeff for the power "+str(n-i)+" : "))
        poly.append(x)

    return poly

def display(poly):
    for i in range(len(poly)):
        if(i!=len(poly)-1):
            print(str(poly[i])+"x^"+str(len(poly)-i),"+ ",end=" ")
        else:
            print(poly[i])

def add(p1,p2):
    poly=[]
    i=0
    j=0
    if(len(p1)>len(p2)):
        while(len(p2)+i < len(p1)):
            poly.append(p1[i])
            i+=1
    else:
        while(len(p1)+j < len(p2)):
            poly.append(p2[j])
            j+=1
    
    while(i<len(p1) and j<len(p2)):
        poly.append(p1[i]+p2[j])
        j+=1
        i+=1

    return poly

def multiply(p1,p2):
    poly=[0]*(len(p1)+len(p2))
    for i in range(len(p1)):
        val=p1[i]
        for j in range(len(p2)):
            poly[i+j]+=val*p2[j];

    return poly

poly1 = [3,2,1]
display(poly1)
poly2 = [4,5,6,3,2,1]
display(poly2)

added_poly=add(poly1,poly2)
display(added_poly)

multiplied=multiply(poly1,poly2)
display(multiplied)