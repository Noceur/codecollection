def digitalSum(n):
    if n < 10 :
        return n
    return n % 10 + digitalSum( n // 10 )
    

def loopdigitalSum(n):
    #print (n)
    while n > 10:
        n = digitalSum(n)
        #print (n)
    return n

#print (loopdigisum(994))
#a = (loopdigitalSum(994))
#print (a)



def digitalSum2(n):
    #if n < 10 :
    #    return n
    n = n % 10 + digitalSum( n // 10 )
    while n > 10:
        n = digitalSum(n)
    return n
    

print (digitalSum2(9992))



24

6