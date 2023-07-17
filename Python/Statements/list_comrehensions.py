mystring = 'list'

mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)


###################instead of this################


newlist = [ letter for letter in mystring]
print('new list',newlist)
#cel to fahrenheit
cel = [0,10,20,34.5]
fah = [((9/5)*temp + 32) for temp in cel]
print(fah)



result = [ 'EVEN' if x%2==0 else 'ODD' for x in range(0,11)]
print(result)



#####################
mynolist = []
for x in [2,4,6]:
    for y in [1,2,1000]:
        mynolist.append(x*y)

print(mynolist)

#now using list comprehensions

mylistyz = [x*y for y in [1,2,1000] for x in [2,4,6]]
print('mylistyz',mylistyz)

mylistxy = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylistxy)