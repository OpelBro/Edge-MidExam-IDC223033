#Creat a function named remove duplicates
def remove_duplicates(nums): 
    unique_nums = []  # Create an empty list to store unique elements
    # Iterate through each number in the original list
    for num in nums:
        # Check if the number is already in the unique list
        found = False
        for unique in unique_nums:
            if num == unique:
                found = True
                break
        
        # If the number is not found in the unique list, add it
        if not found:
            unique_nums.append(num)
    
    return unique_nums

# Example usage
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]