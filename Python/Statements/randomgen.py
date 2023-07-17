from random import shuffle

mylist = [1,2,3,4,5,6,7,9,10]
print(mylist)

#this dont print anything it won't work 
randlist = shuffle(mylist) 
print(randlist)


shuffle(mylist) #this is inplace funtion whihc means it will make permant chnge
print(mylist)


from random import randint
#it will return random number
print(randint(0,100))