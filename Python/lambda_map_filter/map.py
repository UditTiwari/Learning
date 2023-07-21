# filter() is used to select specific elements from an iterable based on a condition,
# while map() is used to transform (map) each element of an iterable using a given function.

def square(num):
    return num**2


my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)
    
#another way if w ewant list
print(list(map(square,my_nums)))




############# print even in the len is ven else one character of the name
def spilcer(mystring):
    if len(mystring)%2 == 0:
        return 'Even'
    else:
        return mystring[0]
    
    
names = ['udit','max','someone']
print(list(map(spilcer,names)))