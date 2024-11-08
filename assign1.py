#Added these new lines of code to learn git and github


from statistics import mode
n = int(input("Enter the number of students"))
marks = []
for i in range(n):
    m = int(input("Enter the marks"))
    marks.append(m)

#average of marks
avgmark = 0
for j in range(n):
    if(marks[j]>0):
        avgmark += marks[j]

print("average marks:",(avgmark/n))
print("Highest marks:",max(marks))

lowestmrk = marks[0]
for i in range(n):
    if(marks[i]>=0 and marks[i]<lowestmrk):
        lowestmrk=marks[i]
print("Lowest marks: ",lowestmrk)

absentcnt=0
for j in range(n):
    if (marks[j]<0):
        absentcnt+=1
print ("Number of absent students: ",absentcnt)

passed = 0
for i in range(n):
    if(marks[i]<35):
        passed+=1
print("Number of students failed: ",passed)
print("Number of students passed",(n-passed))
print("Marks wiht highest frequency: ",mode(marks))