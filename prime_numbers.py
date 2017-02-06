
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
    prime_nos_list = []
    for i in range(n + 1):
        is_prime = True
        divisor = 2
        while divisor < i:
            if i % divisor == 0:
                is_prime = False
                divisor += 1
            else:
                divisor += 1
        if is_prime and not i == 0 and not i == 1:
            prime_nos_list.append(i)
        else:
            is_prime = True
    return prime_nos_list
        
