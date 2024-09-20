# m1 = int(input("Enter the number of rows: "))
# n1 = int(input("Enter the number of columns: "))
# mat1 = list()
# for i in range(m1):
#     newlist = list()
#     for j in range(n1):
#         newlist.append(int(input(f"Enter the ({i+1},{j+1}) element of the matrix: ")))
#     mat1.append(newlist)

# m2 = int(input("Enter the number of rows: "))
# n2 = int(input("Enter the number of columns: "))
# mat2 = list()
# for i in range(m2):
#     newlist = list()
#     for j in range(n2):
#         newlist.append(int(input(f"Enter the ({i+1},{j+1}) element of the matrix: ")))
#     mat2.append(newlist)

m1 = 4
n1 = 3
mat1 = ((1,2,3),(4,5,6),(10,11,1))

m2 = 3
n2 = 4
mat2 = ((1,4,10),(2,5,11),(3,6,12))

def diagonalsum(mat1):
    if(len(mat1)==len(mat1[0])):
        sum = 0
        for i in range(len(mat1)):
            sum += mat1[i][i]
        return sum
    else:
        return "Diagonal sum is not possible."

def add(mat1,mat2):
    addlist = list()
    if(len(mat1)==len(mat2) and len(mat1[0])==len(mat1[0])):
        for i in range(len(mat1)):
            sublist = list()
            for j in range(len(mat1[0])):
                sublist.append(mat1[i][j]+mat2[i][j])
            addlist.append(sublist)
        return addlist
    else:
        return "Sum is not poosible."
    
def sub(mat1,mat2):
    addlist = list()
    if(len(mat1)==len(mat2) and len(mat1[0])==len(mat1[0])):
        for i in range(len(mat1)):
            sublist = list()
            for j in range(len(mat1[0])):
                sublist.append(mat1[i][j]-mat2[i][j])
            addlist.append(sublist)
        return addlist
    else:
        return "Sub is not poosible."
    
def multi(mat1,mat2):
    if (len(mat1[0])==len(mat2)):
        result = [[0 for x in range(len(mat2[0]))] for y in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                for z in range(len(mat2[0])):
                    result[i][z]+= mat1[i][j]*mat2[j][z]
        return result
    else:
        return "Multi is not possible."

def transpose(mat1):
    a=[[0 for x in range(len(mat1[0]))] for y in range(len(mat1))]  
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            a[j][i]=mat1[i][j]
    return a

def typeoftriagular(mat1):
    count = 0
    if (len(mat1)!=len(mat1[0])):
        print("Not a square matrix.")
    else:
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                if (j>i and mat1[i][j]!=0):
                    count+=1
    if (count > 0):
        return "Mat is not lower triangular."
    else:
        return "Mat is lower triangular."

print("Diagonal sum of mat1: ",diagonalsum(mat1))
print("Diagonal sum of mat2: ",diagonalsum(mat2))
print("Addition of mat1 and mat2: ",add(mat1,mat2))
print("Subtraction of mat1 and mat2: ",sub(mat1,mat2))
print("Multiplication of mat1 and mat2: ",multi(mat1,mat2))
print("Transpose of mat1: ",transpose(mat1))
print("Transpose of mat2: ",transpose(mat2))
print("Type of mat1: ",typeoftriagular(mat1))
print("Type of mat2: ",typeoftriagular(mat2))