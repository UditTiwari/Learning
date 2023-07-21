# filter() is used to select specific elements from an iterable based on a condition,
# while map() is used to transform (map) each element of an iterable using a given function.

def check_even(num):
    return num % 2 == 0

mynums = [1,2,3,4,5,6]

print(list(filter(check_even,mynums)))

for n in filter(check_even,mynums):
    print(n)
    
