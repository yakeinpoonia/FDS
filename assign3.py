m1 = int(input("Enter the number of rows: "))
n1 = int(input("Enter the number of columns: "))
matrix1 = list()
for i in range(m1):
    newlist = list()
    for j in range(n1):
        newlist.append(int(input(f"Enter the ({i+1},{j+1}) element of the matrix: ")))
    matrix1.append(newlist)

m2 = int(input("Enter the number of rows: "))
n2 = int(input("Enter the number of columns: "))
matrix2 = list()
for i in range(m2):
    newlist = list()
    for j in range(n2):
        newlist.append(int(input(f"Enter the ({i+1},{j+1}) element of the matrix: ")))
    matrix2.append(newlist)

def diagonalsum(mat1,m1,n1):
    sum = 0
    for i in range(m1):
        for j in range(n1):
            if(i==j):
                sum+=mat1[i][j]
    return sum

def add(mat1,m1,n1,mat2,m2,n2):
    addlist = list()
    if(m1==m2 and n1==n2):
        for i in range(m1):
            sublist = list()
            for j in range(n1):
                sublist.append(mat1[i][j]+mat2[i][j])
            addlist.append(sublist)
        return addlist
    else:
        return "Sum is not poosible."
    
def sub(mat1,m1,n1,mat2,m2,n2):
    addlist = list()
    if(m1==m2 and n1==n2):
        for i in range(m1):
            sublist = list()
            for j in range(n1):
                sublist.append(mat1[i][j]-mat2[i][j])
            addlist.append(sublist)
        return addlist
    else:
        return "Sub is not poosible."
    
def multi(mat1,m1,n1,mat2,m2,n2):
    if (n1==n2):
        addlist = list()
        for i in range(n1):
            yakein = mat1[]
    else:
        return "Multi is not possible."


print(add(matrix1,m1,n1,matrix2,m2,n2))