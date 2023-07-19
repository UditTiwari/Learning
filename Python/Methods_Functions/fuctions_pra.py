def lesser_of_two_evens(a,b):
    if a%2 ==0 and b% 2 == 0:
        #Both number are even
        if a <b:
            result = a
        else:
            result = b
    else:
        #One or both numbners are ODD
        if a>b:
            result = a
        else:
            result = b
    
    return result


print(lesser_of_two_evens(4,3))



#Better way to do
def lesser_of_two_evens(a,b):
    if a%2 ==0 and b% 2 == 0:
        #Both number are even
        return min(a,b)
    else:
        #One or both numbners are ODD
        return min(a,b)
    
    


print(lesser_of_two_evens(6,3))
