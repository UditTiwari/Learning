#Alomost there Given an integer n ,return True if n is within 10 of either 100 or 200



def alomost_there(n):
    return (abs(100-n)<=10) or (abs(200-n)<=10)

print(alomost_there(110))