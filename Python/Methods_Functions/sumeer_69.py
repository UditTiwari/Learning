def summer_69(arr):
    total = 0 
    add = True
    
    for num in arr:
        while add:
            if num != 6:
                print(num)
                total += num
                break
            else:
                add = False
        while not add :
            if num != 9 :
                break
            else:
                add = True
                break
    return total
                
    



# print(summer_69([1,3,5])) #output--> 9

print(summer_69([4,5,6,7,8,9])) #output-->9

# print(summer_69([4,5,5,6,9,8,7])) #output-->29