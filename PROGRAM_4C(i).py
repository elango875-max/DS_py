buildingconstructions=['bricks', 'cement', 'sand', 'water', 'gravels', 'steel']
print(buildingconstructions)
print(buildingconstructions[0])
print(buildingconstructions[1])
print(buildingconstructions.index('sand'))
print(len(buildingconstructions))
buildingconstructions.append('wood')
print(buildingconstructions)
buildingconstructions.insert(2,'marbles')
print(buildingconstructions)
buildingconstructions.remove('wood')
print(buildingconstructions)
buildingconstructions.pop(2)
print(buildingconstructions)
buildingconstructions[2]='tiles'
print(buildingconstructions)
buildingconstructions.sort()
print("After sorting: ",buildingconstructions)
buildingconstructions.reverse()
print("Reversedlist: ", buildingconstructions)
New = buildingconstructions[:]
print(New)
x = slice(2)
print(buildingconstructions[x])
test_list1 = ['bricks', 'cement', 'sand', 'water', 'gravels', 'steel']
test_list2 = ['sand','wood','marbles','tiles']
for i in test_list2 :
   test_list1.append(i)
   print("Concatenated list using naive method : ", str(test_list1))