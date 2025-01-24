def find_smallest_element(nums):
    smallest = nums[0]
    
    for num in nums[1:]:
        if num < smallest:
            smallest = num
    
    return smallest
nums = [10, 20, 5, 40, 15]
smallest = find_smallest_element(nums)
print(f"The smallest element in the list is: {smallest}")

#The smallest element in the list is: 5