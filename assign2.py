total = int(input("Total number of students: "))
cric = int(input("Number of students playing cricket:"))
badminton =  int(input("Number of students playing badminton: "))
football = int(input("Number of students playig football: "))

cric_list = [2]
badminton_list = []
football_list = []

for i in range(cric):
    x = int(input(f"Enter the {i+1} student roll no. who play cricket: "))
    cric_list.append(x)
for i in range(badminton):
    x = int(input(f"Enter the {i+1} student roll no. who play badminton: "))
    badminton_list.append(x)
for i in range(football):
    x = int(input(f"Enter the {i+1} student roll no. who play football: "))
    football_list.append(x)

def union(li1,li2):
    li3 = li1.copy()
    for i in range(len(li2)):
        if li2[i] not in li1:
            li3.append(li2[i])
    return li3

def intersection(li1,li2):
    li3 = []
    for i in range(len(li1)):
        if li1[i] in li2:
            li3.append(li1[i])
    return li3

def difference(li1,li2):
    li3 = li1.copy()
    for i in range(len(li2)):
        if li2[i] in li3:
            li3.remove(li2[i])
    return li3

ab_intersection = intersection(cric_list,badminton_list)
ab_union = union(cric_list,badminton_list)
abc_intersection = intersection(ab_intersection,football_list)
abc_union = union(ab_union,football_list)

print(cric_list)
print(badminton_list)
print(football_list)
print(ab_union)
print(ab_intersection)
print("List of students who play both cricket and badminton: ",ab_intersection)
print("List of students who either play cricket or badminton but not both: ",difference(ab_union,ab_intersection))
print("No of students who neither play cricket nor badminton: ",len(difference(football_list,ab_union)))
print("No of students who play cricket and football but not badminton: ",difference(intersection(cric_list,football_list),abc_intersection))
print("No of students who don't play any game: ",total-len(abc_union))
print("List of students who play atleast one game: ", abc_union)
print("List of students who play all the game: ", abc_intersection)