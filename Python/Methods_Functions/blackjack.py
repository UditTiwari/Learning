#Given three int bw 1 to 11 ,if the their sum is less than or equal to 21 return thier sum.if thier sum exceeds 21 and theres an eleven ,reduce the total sum by 10.Finaly ,if the sum(even after adjjustment) exceeds 21,return 'BUST

def blackjack(a,b,c):
    if sum([a,b,c])<= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c]) - 10
    else:
        return 'BUST'
        


print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))