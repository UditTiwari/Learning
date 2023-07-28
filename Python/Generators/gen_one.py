#Use to save memory also
#used Yield instead of return



def create_cubes(n):
    for x in range(n):
        yield x**3
        
        
for i in create_cubes(10):
    print(i)
    
    
#next()