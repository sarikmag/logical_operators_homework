def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x=a//10000
    y=a//1000%10
    c=a//100%10
    d=a//10%10
    f=a%10000%10
    
    return x>y>c>d>f
print(main(95432))