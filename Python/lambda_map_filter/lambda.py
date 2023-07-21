# def square(num):
#     # result = num ** 2
#     return num ** 2


#this can also written as like this
 ####-------def square(num): return num ** 2


#using lambda exp
square = lambda num: num ** 2


print(square(3))


#using map with lambda exp
mylist = [1,2,3,4,5]
print(list(map(lambda num: num ** 2,mylist)))


names = ['Andy','Eve','Sally']

print(list(map(lambda x:x[0],names)))

#print the reverse name 
print(list(map(lambda x:x[::-1],names)))
