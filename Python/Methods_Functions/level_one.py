#LEVEL ONE PROBLEMS
#WRITE A FUNCTION THAT CAPITALIZES THE FIRST AND FOURTH LETTERS OF A NAME
 #old_macdonal('macdonald) --> MacDonald
 
# def old_macdonald(name):
#     first= name[0]
#     inbetween = name[1:3]
#     fourth = name[3]
#     rest = name[4:]
    
#     return first.upper() + inbetween + fourth.upper() + rest
     
     
def old_macdonald(name):
    first_half= name[:3]
    second_half =name[3:]
    
    
    return first_half.capitalize() + second_half.capitalize()
     
     
print(old_macdonald('macdonald'))

