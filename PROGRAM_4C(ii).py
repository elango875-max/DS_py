buildingconstruction=('bricks', 'cement', 'sand', 'water', 'gravels', 'steel')
print('Our tuple is:',buildingconstruction)
print('Item in the first positionis: ',buildingconstruction[0])
print('Item in the 5th position is: ',buildingconstruction[4])
indexOfwater=buildingconstruction.index('water')
print('Index of water is: ', indexOfwater)
Tuplelength=len(buildingconstruction)
print('Length of thebuildingconstruction tuple is: ',Tuplelength)
for item in buildingconstruction:
    print(item)
    print(buildingconstruction*2)
    print(buildingconstruction[1:4])
if "brick" in buildingconstruction:
    print("bricks is available in the buildingconstruction tuple")
else:
    print("bricks is not available in the buildingconstruction tuple")