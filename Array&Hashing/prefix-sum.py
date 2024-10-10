# Creating a class PrefixSum that takes an array and create a prefix sum array of this

class PrefixSum:
    def __init__(self,nums):
        self.prefix = []
        total = 0

        for i in nums:
            total += i
            self.prefix.append(total)

nums = [1,2,3,4,5,6,7,8,9]

prefix_num = PrefixSum(nums).prefix

# I want to calculate the sum between left_index = 1 (included) and right_index = 5
# firsly get the right index in prefix sum 
right_sum = prefix_num[5]

# get the left index - 1 because we need to include the left indx element into sum
left_index = 1
left_sum = 0
if left_index > 0:
    left_sum = prefix_num[left_index-1]

sum_of_the_subarray = right_sum - left_sum

print("sum of sub array : " ,sum_of_the_subarray)