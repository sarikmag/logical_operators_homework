def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x=a//100
    y=a//10%10
    z=a%100%10
    s=x+y+z
    
    return s%2==1
print(main(335))