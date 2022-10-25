def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    x=n//10000
    y=n//1000%10
    c=n//100%10
    d=n//10%10
    f=n%10000%10
    print(x,y,c,d,f)
    return  x
print(main(10011))