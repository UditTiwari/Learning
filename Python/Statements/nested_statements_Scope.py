#LEGB RULE
#L : Local  , E: Enclosing function locals  ,G : Global  , B : Built-in

lambda num :num**2 #Local


#GLOBAL
name = "this is a global string"

def greet():
    #ENCLOSING
    name = 'Sammy'  
    
    def hello():
        #LOCAL
        name = "I am Local"
        print('hello '+ name)
        
    hello()
    
greet()


