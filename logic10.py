def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    if a//10<10 and a//10>0:
        return True
    return False
print(main(12))