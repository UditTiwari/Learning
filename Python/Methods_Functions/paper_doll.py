#Given a string,return a string where for evry character in the original there are three characters
#paper_doll('Hello) --> 'HHeellllllooo'


def paper_doll(text):
    result = ''
    for char in text:
        result += char*3
        
    return result
        
    
    
    
    
print(paper_doll('Hello'))