carparts =['Engine', 'Transmission', 'Wheel', 'Gear', 'Brake', 'Battery']
print(carparts)
print(carparts[0])
print(carparts[1])
print(carparts.index('Wheel'))
print(len(carparts))
carparts.append('Headlights')
print(carparts)
carparts.insert(2,'Radiator')
print(carparts)
carparts.remove('Headlights')
print(carparts)
carparts.pop(2)
print(carparts)
carparts[2]='Tyre'
print(carparts)
carparts.sort()
print("After sorting: ",carparts)
carparts.reverse()
print("Reversedlist: ", carparts)
New = carparts[:]
print(New)
x = slice(2)
print(carparts[x])
test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]
for i in test_list2 :
   test_list1.append(i)
   print("Concatenated list using naive method : ", str(test_list1))