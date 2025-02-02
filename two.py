import random


def randomized_binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = random.randint(left, right)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
