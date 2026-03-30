no_of_terms =int(input("Enter number of values:"))
list1 = []
for val in range(0,no_of_terms,1):
 num =int(input("Enter integer:"))
list1.append(num)
print("Circulatingthe elementsof list",list1)
for val in range(0,no_of_terms,1):
 num = list1.pop(0)
list1.append(num)
print(list1)