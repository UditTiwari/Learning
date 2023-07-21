x = 50

# def func(x):
#     print(f'X is{x}')
    
    
#     x = 200
#     print(f'its local var {x}')
    
    
# re = func(x)


# def func():
#     global x
#     print(f'X is {x}')
    
    
#     x = 200
#     print(f'its local var {x}')
    
    
# re = func()


def func(x):
    # global x
    print(f'X is {x}')
    
    
    x = 200
    print(f'its local var {x}')
    return x
    
#better way to use insted of global using reassigment
x = func(x)
print(x)