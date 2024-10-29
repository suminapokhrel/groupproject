def find_largest_number(numbers):
    if not numbers:
        return None #returns none if the list is empty
    
    largest = numbers [0]
    for numbers in numbers:
        if number > largest:
            largest = number
    return largest


# example

numbers_list = [3, 1, 4, 1, 7, 2, 9, 5, 8, 6]
largest_number = find_largest_number(numbers_list)
print("The largest number is:", largest_number)