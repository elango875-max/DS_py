integers = [1, 16, 3, 39, 26, 4, 8, 16]
copy_of_integers = integers[:]
largest_integer = max(copy_of_integers)
copy_of_integers.remove(largest_integer)
second_largest_integer =max(copy_of_integers)
print(largest_integer)
print(second_largest_integer)