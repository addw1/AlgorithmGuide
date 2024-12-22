def weave_array(numbers):
    n = len(numbers)
    left = 0
    right = n - 1
    result = []

    while left <= right:
        # Take from the left pointer
        result.append(numbers[left])
        left += 1

        # Check if we still have elements left on the right side
        if left <= right:
            result.append(numbers[right])
            right -= 1

    return result


# Example usage:
numbers = [10, 20, 30, 40, 50, 60]
print(weave_array(numbers))
# Output: [10, 60, 20, 50, 30, 40]
