def inp():
    n = int(input("Enter Row : "))
    m = int(input("Enter Column : "))
    matrix = []
    for i in range(n):
        list=[]
        for j in range(m):
            x=int((input("Enter value : ")))
            list.append(x)
        matrix.append(list)

    return matrix

def sparse_making(m):
    matrix = []
    temp=[]
    temp.append(len(m))
    temp.append(len(m[0]))
    temp.append(0)
    matrix.append(temp)
    cnt=0

    for i in range(len(m)):
        for j in range(len(m[0])):
            if(m[i][j]!=0):
                temp=[]
                temp.append(i)
                temp.append(j)
                temp.append(m[i][j])
                matrix.append(temp)
                cnt+=1


    matrix[0][2]=cnt
    return matrix

def sparse_output(m):
    print("Row","Col","Value")
    for i,j,v in m:
        print(i," ",j," ",v)

def transpose(m):
    matrix=[]
    temp=[]
    temp.append(0)
    temp.append(0)
    temp.append(0)
    matrix.append(temp)

    for i in range(1,m[0][2]+1):
        temp=[]
        temp.append(m[i][1])
        temp.append(m[i][0])
        temp.append(m[i][2])
        matrix.append(temp)

    matrix.sort()
    matrix[0][0]=m[0][1]
    matrix[0][1]=m[0][0]
    matrix[0][2]=m[0][2]

    return matrix

def fast_transpose(m):
    print("Fast Transpose")
    f=[0]*(m[0][1])

    for i in range(m[0][2]):
        f[m[i+1][1]]+=1

    s=[]
    s.append(1)
    for i in range(len(f)-1):
        s.append(s[i]+f[i])
    
    matrix=[]
    temp=[]
    temp.append(m[0][1])
    temp.append(m[0][0])
    temp.append(m[0][2])
    matrix.append(temp)

    for i in range(m[0][2]):
        temp=[]
        temp.append(0)
        temp.append(0)
        temp.append(0)
        matrix.append(temp)

    for i in range(m[0][2]):
        matrix[s[m[i+1][1]]][0]=m[i+1][1]
        matrix[s[m[i+1][1]]][1]=m[i+1][0]
        matrix[s[m[i+1][1]]][2]=m[i+1][2]
        s[m[i+1][1]]+=1

    return matrix

def added(m1,m2):
    print("Addition")
    if(m1[0][1] != m2[0][1]  or m2[0][1] != m2[0][1]):
        print("Addition not possible")
    else:
        matrix=[]
        temp=[]
        temp.append(m1[0][0])
        temp.append(m1[0][1])
        temp.append(0)
        matrix.append(temp)
        cnt=0
        i=1
        j=1

        while(i<m1[0][2] and j<m2[0][2]):
            temp=[]
            if(m1[i][0]==m2[j][0]):

                if(m1[i][1]==m2[j][1]):
                    temp.append(m1[i][0])
                    temp.append(m1[i][1])
                    temp.append(m1[i][2]+m2[j][2])
                    i+=1
                    j+=1
                    cnt+=1

                elif(m1[i][1] > m2[j][1]):
                    temp.append(m2[j][0])
                    temp.append(m2[j][1])
                    temp.append(m2[j][2])
                    j+=1
                    cnt+=1
                else:
                    temp.append(m1[i][0])
                    temp.append(m1[i][1])
                    temp.append(m1[i][2])
                    i+=1
                    cnt+=1
            elif(m1[i][0]>m2[j][0]):
                temp.append(m2[j][0])
                temp.append(m2[j][1])
                temp.append(m2[j][2])
                j+=1
                cnt+=1
            else:
                temp.append(m1[i][0])
                temp.append(m1[i][1])
                temp.append(m1[i][2])
                i+=1
                cnt+=1

        
            matrix.append(temp)

    
    while(i<m1[0][2]):
        temp=[]
        temp.append(m1[i][0])
        temp.append(m1[i][1])
        temp.append(m1[i][2])
        i+=1
        cnt+=1
        matrix.append(temp)

    while(j<m2[0][2]):
        temp=[]
        temp.append(m2[j][0])
        temp.append(m2[j][1])
        temp.append(m2[j][2])
        j+=1
        cnt+=1
        matrix.append(temp)

    matrix[0][2]=cnt
    
    return matrix




matrix = (sparse_making(inp()))
sparse_output(matrix)
sparse_output(transpose(matrix))
sparse_output(fast_transpose(matrix))

# 0
# 5
# 0
# 7
# 9
# 0
# 0
# 0
# 0
# 0
# 3
# 0
# 0
# 8
# 0
# 0

