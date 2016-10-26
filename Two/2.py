def fib(n):
    print 'n = ',n
    if n>1:
        return n*fib(n-1)
    else:
        print 'end of the line'
        return 1

# testing modular
if __name__=='__main__':
    for i in xrange(10):
        print '*'*40
        fib(i)
    print '*'*40

    
        
