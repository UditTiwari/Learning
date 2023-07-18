#Check even numbers 
def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass
            #return False #WRONG !!!! it will alwys check the first value only 
    return False
            
    
mylist = [1,2,7]
print(check_even_list(mylist))




#Get All Even numbers





    