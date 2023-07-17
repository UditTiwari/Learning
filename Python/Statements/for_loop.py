# #my_iterable = [1,2,3]
# #for item_name in my_iterable:
#     #print(item_name)
    
    
mylist = [1,2,3,4,5,6,7]

for num in mylist:
    if num % 2 ==0:
        print(num)
    else:
        print(f"Odd number: {num}")
        
        
#Sum the list
list_sum = 0
for num in mylist:
    list_sum += num
    #  print("inside loop",list_sum)

print("Sum",list_sum)



mytuplist = [(1,2),(3,4),(5,6),(7,8)]
# print(len(mytuplist))

# for item in mytuplist:
#     print(item)

# tuple Unpakcing
for a,b in mytuplist:
    print(a) # print first element from all tuple
    # print(b)
    
    
d = {"k1":1,"k2":2,"k3":3}

for item in d:
    print(item)

#now we want item pairs key : value both
for item in d.items():
    print(item)
    
#only value
for value in d.values():
    print(value)
    
#i want key ,valkue in diffrent var (using tuple unpacking)

for key,value in d.items():
    print(key,value)
    
    
    
