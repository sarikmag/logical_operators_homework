def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x=a//10
    y=a%10
    z=x+y
    
    return z%2==1
print(main(35))