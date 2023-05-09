def factoriall(n):
    
    fac = 1
    for factorial in range (fac,n+fac):
        fac = fac*factorial
        return fac
    n = int(input("enter your number: "))
    fac = factoriall(n)
    print(n)