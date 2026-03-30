librarycomp=['books', 'newspaper', 'computer', 'magazine', 'journals']
print(librarycomp)
print(librarycomp[0])
print(librarycomp[1])
print(librarycomp.index('computer'))
print(len(librarycomp))
librarycomp.append('projects')
print(librarycomp)
librarycomp.insert(2,'newsletter')
print(librarycomp)
librarycomp.remove('projects')
print(librarycomp)
librarycomp.pop(2)
print(librarycomp)
librarycomp[2]='library attendance'
print(librarycomp)
librarycomp.sort()
print("After sorting: ",librarycomp)
librarycomp.reverse()
print("Reversedlist: ", librarycomp)
New = librarycomp[:]
print(New)
x = slice(2)
print(librarycomp[x])
test_list1 =['books','newspaper', 'computer', 'magazine', 'journals']
test_list2 = ['project','newsletter']
for i in test_list2 :
   test_list1.append(i)
   print("Concatenated list using naive method : ", str(test_list1))
