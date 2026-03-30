libcomp=('books', 'newspaper', 'computer', 'magazine', 'journals')
print('Our tuple is:',libcomp)
print('Item in the first position is: ',libcomp[0])
print('Item in the 5th position is: ',libcomp[4])
indexOfcomputer=libcomp.index('computer')
print('Index of computer is: ', indexOfcomputer)
Tuplelength=len(libcomp)
print('Length of thelibcomp tuple is: ',Tuplelength)
for item in libcomp:
   print(item)
   print(libcomp*2)
   print(libcomp[1:4])
if "journal" in libcomp:
   print("journals is available in the libcomp tuple")
else:
   print("journals is not available in the libcomp tuple")