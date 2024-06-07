def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    return any([num % 7 == 0 for num in nums])
        
        

print(has_lucky_number([3, 14]))