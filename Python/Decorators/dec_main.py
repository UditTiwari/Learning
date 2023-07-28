def new_decorator(original_func):
    
    def wrap_func():
        
        print("Some extra cdoe ,before the original fuction")
        original_func()
        print('Some extra code,aftr the original fuction')
        
    return wrap_func



# def func_need_decorator():
#     print("I want to be decorated!!!")
    

# decorated_func = new_decorator(func_need_decorator) #but this can done using @

# print(decorated_func())


###the above can be done using @

@new_decorator
def func_need_decorator():
    print("I want to be decorated!!!")
    
    
print(func_need_decorator())