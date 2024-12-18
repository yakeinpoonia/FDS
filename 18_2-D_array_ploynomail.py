def take_input():
    n=int(input("Enter no of terms : "))
    list=[]
    for i in range(n):
        x=int(input("Enter coeffi : "))
        y=int(input("Enter power : "))
        temp=[]
        temp.append(x)
        temp.append(y)
        list.append(temp)
    
    return list

def addition(p1,p2):
    n1=len(p1)
    n2=len(p2)

    added = []
    i,j=0,0
    while(i<n1 and j<n2):
        if(p1[i][1]==p2[j][1]):
            added.append([p1[i][0]+p2[j][0],p1[i][1]])
            i+=1
            j+=1
        elif(p1[i][1]>p2[i][1]):
            added.append(p1[i])
            i+=1
        else:
            added.append(p2[j])
            j+=1
    
    while(i<n1):
        added.append(p1[i])
        i+=1

    while(j<n2):
        added.append(p2[j])
        j+=1

    return added

def multiplication(p1,p2):
    multiplied={}
    for coeff1,term1 in p1:
        for coeff2,term2 in p2:
            exponent = term1+term2
            coeff = coeff1*coeff2

            if(exponent in multiplied):
                multiplied[exponent]+=coeff
            else:
                multiplied[exponent]=coeff
    
    ans = [[coeff,exponent] for exponent,coeff in multiplied.items()]
    ans.sort(key=lambda x:x[1], reverse=True)

    return ans



def display(poly):
    for i in range(len(poly)):
        if(i!=len(poly)-1):
            print(str(poly[i][0])+"x^"+str(poly[i][1])+" + ",end="")
        else:
            print(str(poly[i][0])+"x^"+str(poly[i][1]))


poly1=take_input()
display(poly1)
poly2=take_input()
display(poly2)
adds=addition(poly1,poly2)
display(adds)
multiplies=multiplication(poly1,poly2)
display(multiplies)

# 2
# 3
# 2
# 4
# 1
# 3
# 4
# 3
# 3
# 2
# 2
# 1