def compute():
    inp = int(input("enter the dividend:"))
    inm = int(input("enter the divisor:"))
    try:
            print("the answer is:", inp / inm) 
            
    except ZeroDivisionError:
            print("denominator can't be zero")

compute()