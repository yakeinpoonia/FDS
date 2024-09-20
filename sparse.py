def inputS():
    n = int(input("Enter th no of rows: "))
    m = int(input("Enter th no of cols: "))
    sparse = []
    count = 0
    for i in range(0,n):
        for j in range(0,m):
            a = int(input(f"Enter {i},{j} element: "))
            if a!=0:
                sparse.append([i,j,a])
                count+=1
    sparse = [[n,m,count]] + sparse
    return sparse


def simpleTrans(mat):
    transMat = [] + mat[:1]
    for i in range(0,mat[0][1]):
        for j in range(1,mat[0][2]+1):
            if mat[j][1]==i:
                transMat.append([mat[j][1],mat[j][0],mat[j][2]])
    return transMat

def addition(mat, mat2):
    addMat = []
    i, j = 0, 0
    
    while i < len(mat) and j < len(mat2):
        if mat[i][0] == mat2[j][0] and mat[i][1] == mat2[j][1]:
            # Both entries have the same row and column
            addMat.append([mat[i][0], mat[i][1], mat[i][2] + mat2[j][2]])
            i += 1
            j += 1
        elif (mat[i][0] < mat2[j][0]) or (mat[i][0] == mat2[j][0] and mat[i][1] < mat2[j][1]):
            # mat1 entry is smaller
            addMat.append([mat[i][0], mat[i][1], mat[i][2]])
            i += 1
        else:
            # mat2 entry is smaller
            addMat.append([mat2[j][0], mat2[j][1], mat2[j][2]])
            j += 1
    
    # Add remaining elements from mat1
    while i < len(mat):
        addMat.append([mat[i][0], mat[i][1], mat[i][2]])
        i += 1
    
    # Add remaining elements from mat2
    while j < len(mat2):
        addMat.append([mat2[j][0], mat2[j][1], mat2[j][2]])
        j += 1
    
    return addMat



def fastTranspose(sp1):
    sp2 = [[sp1[0][1],sp1[0][0],sp1[0][2]]] + [0]* sp1[0][2]
    freq = [0] * (sp1[0][1])
    ind = [0] * (sp1[0][1])
    ind[0]=1
    for i in sp1[1:]:
        freq[(i[1])] += 1
    for i in range(1,len(freq)):
        ind[i] = ind[i-1]+freq[i-1]
    for i in sp1[1:]:
        sp2[ind[i[1]]] = [i[1],i[0],i[2]]
        ind[i[1]]+=1
    return sp2

        
menu = "Choose from the below\n \
    1.Add\n \
    2.Simple transpose\n \
    3.Fast Transpose"


# sp1 = inputS()
sp1 = [[3,3,4],[0,1,1],[1,2,2],[2,0,3],[2,2,1]]
for i in sp1:
    print(i)
print()
print(menu)
option = int(input("Enter the option: "))

if option==1:
    sp2 = inputS()
    for i in addition(sp1,sp2):
        print(i)
elif option==2:
    for i in simpleTrans(sp1):
        print(i)
if option==3:
    for i in fastTranspose(sp1):
        print(i)