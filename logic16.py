def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    if a//10000>0 and a//10000<10:
        return True
    return False
print(main(15234))