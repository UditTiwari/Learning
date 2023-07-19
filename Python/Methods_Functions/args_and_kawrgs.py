


def myfunc(a,b):
    #Return 5% of the sum of a and b
    return sum((a,b)) * 0.05

print(myfunc(40,60))

#Using *args we dont need to give paramerts they can pass as many as they pass now using this

def myfunc(*args):
    #Return 5% of the sum of a and b
    return sum(args) * 0.05

print(myfunc(40,60))

#how dict works
dictlist = {'k1':1,'k2':2}
# if 'k2' in dictlist:
#     print('present')

#**kwrgs retrun a dictionary
def mykwfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
        

mykwfunc(fruit='apple')



# 
   