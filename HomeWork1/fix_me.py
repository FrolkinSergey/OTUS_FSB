"""Module docstring"""


def calculate_average(nums):
    """Return average"""
    total = sum(nums)
    count = len(nums)
    total / count


nums2 = [10, 15, 20]
RESULT = calculate_average
print("The average is:", RESULT)
