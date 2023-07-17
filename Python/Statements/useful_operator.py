index_count =0 

for letter in 'abcde':
    # print('At index {} the letter is {}'.format(index_count,letter))
    index_count +=1
    
    
#if we want to get words 
index_count =0 
word = 'abcde'
for letter in word:
    # print(word[index_count]) #we get index number now normally how we acces element in list we can do like that list[index_number]
    index_count +=1
    
    
#Instead of this we use enumerate
word = 'abcde'
for item in enumerate(word):
    print(item)#Result will be tuple containg (index,value)
    
    
word = 'abcde'
for index,letter in enumerate(word):
    print(index,letter)


#ZIP 
mylistone=[1,2,3]
mylisttwo=['a','b','c']

for item in zip(mylistone,mylisttwo):
    print(item) #return tuples
    
#In keyword

check = 2 in [1,2,3]
print(check)
check = 'x' in ['t','x','z']f

checkdic = 'mykey' in {'mykey':345}
print(checkdic)

cdic = {'mykey':345}
keyvalue = 345 in cdic.values()
if keyvalue:
    print("Present")