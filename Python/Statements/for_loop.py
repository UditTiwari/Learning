#my_iterable = [1,2,3]
#for item_name in my_iterable:
    #print(item_name)
    
    
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