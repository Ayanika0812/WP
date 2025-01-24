class PairSumFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_pair(self, target):
        # Create a dictionary to store numbers and their indices
        num_indices = {}
        
        # Iterate through the list
        for index, num in enumerate(self.numbers):
            complement = target - num  # Find the complement needed to reach the target sum
            
            # Check if the complement exists in the dictionary
            if complement in num_indices:
                return (num_indices[complement], index)  # Return the pair of indices
            
            # If complement doesn't exist, store the number and its index in the dictionary
            num_indices[num] = index
        
        return None  # Return None if no pair is found

# Example usage
numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50

# Creating an instance of PairSumFinder
pair_finder = PairSumFinder(numbers)

# Finding the pair of indices
result = pair_finder.find_pair(target)

# Printing the result
if result:
    print(f"The indices of the pair whose sum equals {target} are: {result[0]}, {result[1]}")
else:
    print(f"No pair found whose sum equals {target}.")
#The indices of the pair whose sum equals 50 are: 2, 3
