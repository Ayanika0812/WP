from itertools import combinations

class SubsetGenerator:
    def __init__(self, nums):
        self.nums = nums

    def get_subsets(self):
        subsets = []
        for i in range(len(self.nums) + 1):
            for subset in combinations(self.nums, i):
                subsets.append(list(subset))
        return subsets

# Hardcoded input
nums = [4, 5, 6]

# Creating an instance of SubsetGenerator
subset_generator = SubsetGenerator(nums)

# Getting all subsets
result = subset_generator.get_subsets()

# Printing the result
print("All possible unique subsets:")
print(result)


#All possible unique subsets:
# [[], [4], [5], [4, 5], [6], [4, 6], [5, 6], [4, 5, 6]]
