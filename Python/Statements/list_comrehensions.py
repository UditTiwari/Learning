mystring = 'list'

mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)


###################instead of this################


newlist = [ letter for letter in mystring]
print('new list',newlist)