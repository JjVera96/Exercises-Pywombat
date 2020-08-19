def items_duplicate(nums):
    set_nums = set(nums)
    return len(set_nums) == len(nums)

print(items_duplicate([1, 2, 3, 4, 5]))
print(items_duplicate([1, 2, 3, 4, 5, 5]))
print(items_duplicate([1, 2, 3, 2]))