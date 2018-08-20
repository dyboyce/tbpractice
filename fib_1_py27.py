def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
#this is bad, will goto n! 


def F2():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b


retval = F(7)
print(retval)


#n limit
#num1
#num2
#add 1 to 2
#check if we hit our N limit, increment
#plug sum back into whole thing


