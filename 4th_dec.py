#if-else
age = int(input("Enter the age:"))
if(age>=10):
    print("Yes")
elif(age==1):
    print("Yes")
else:
    print("No")
#match-making
a = int(input("Enter a number:"))

match a:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case _:
        print("NO match foubd")
#for-loop
for i in range(5):
    print(i+1)
print("printing set..")
a = [1,34,456,34,234]
s = {3,23,233}
for item in s:
    print((item)+1)
for item in a:
    print((item)+3)  
#while-loop
i = 0
while(i<10):
    print(i)
    i +=1
    
