#Given a sentence,return a sentence with the words reversed
#master_yoda('I am home) --> 'home am I


def master_yoda(text):
    wordlist = text.split(' ')
    reverse_wordlist = " ".join(wordlist[::-1])
    return reverse_wordlist
        
        
    


print(master_yoda('I am home'))
    