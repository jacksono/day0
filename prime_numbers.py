
def prime_numbers(n):
    '''
    Generates prime numbers in a range between 0 and a given positve number
    Args:
        Takes 1 argument for the upper limit of the range
    Returns:
        Returns a list containing all prime numbers in the range
    '''
    if not isinstance(n, int):
        return "Invalid input type"
    if n < 0:
        return 'Invalid input, negative number entered'

