def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    total =0
    evens_counter = 0
    
    for char in nums:
        if char%2 ==0:
            evens_counter+1
            if total ==0:
                total+=char
            else:
                total *=char
            
    if evens_counter == 0 and total == 0:
        total =1


    return total

print(multiply_even_numbers([2, 4, 5]))