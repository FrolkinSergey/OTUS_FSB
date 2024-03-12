"""Module docstring"""


def calculate_average(nums):
    """Return average"""
    total = sum(nums)
    count = len(nums)

    return total / count


nums2 = [10, 15, 20]
RESULT = calculate_average(nums2)
print("The average is:", RESULT)
