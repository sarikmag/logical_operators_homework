def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    if a//100<10 and a//100>0:
        return True
    return False
print(main(123))