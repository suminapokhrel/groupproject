def find_largest_number(numbers):
    if not numbers:
        return None #returns none if the list is empty
    
    largest = numbers [0]
    for numbers in numbers:
        if number > largest:
            largest = number
    return largest


