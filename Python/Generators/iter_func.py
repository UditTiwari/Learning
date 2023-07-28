s = 'hello'

for letter in s:
    print(letter)
    
    
#to turn STRING IN interator use --->iter()

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
