#Find 33 GIven a list of ints ,return True if the array contains a 3 next to a 3 somwwhere


def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] ==3 and nums[i+1] == 3:
            return True
        
    return False

def improve_has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i:i+2] == [3,3]:
            return True
        
    return False
        
        
    
    
    

# mylist = [1,2,3,3]
print(has_33([1,2,3,3]))

print(improve_has_33([1,2,3,3]))