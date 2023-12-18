name = 'Kiriti'
print(name)

print(name[0:3]) #start from 0 and go till 2
print(name[1:4])
print(name.upper())
print(name.capitalize())
print(name.count("K"))
print(name.isnumeric())
 
a1 = 'kiriti'
a2 = "kiriti"
a3 = '''kiriti
good girl'''
print(a1, a2, a3)

l1 = [1,2,3,4,5,6, "Kiriti"]
print(type(l1))
print(l1)
l1.remove("Kiriti")
l1.extend([2,3,44])
print(l1)
#Tuples
t = (3,5,23,23)
print(t.count(23))
print(t.index(5)) #position of that tuples element 
#tuples and  string is immutable

#set
a1 = {3,5,13,23,13,5,5}
a2 = {3,5}
print(a1.pop()) #remove random element

#dictionary is mutable
a = {}
b = set()
print(a, type(a))
print(b, type(b))
#keys:values
