def binary_search(arr: list[int], target: int) -> int:
    """Return any index where value == target in a sorted array, or -1 if missing."""
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def first_occurrence(arr: list[int], target: int) -> int:
    """Return the first index where value == target, or -1 if missing."""
    index = lower_bound(arr, target)
    if index < len(arr) and arr[index] == target:
        return index
    return -1


def last_occurrence(arr: list[int], target: int) -> int:
    """Return the last index where value == target, or -1 if missing."""
    index = upper_bound(arr, target) - 1
    if index >= 0 and arr[index] == target:
        return index
    return -1


def lower_bound(arr: list[int], target: int) -> int:
    """Return the first index where value >= target."""
    start = 0
    end = len(arr)

    while start < end:
        mid = (start + end) // 2

        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1

    return start


def upper_bound(arr: list[int], target: int) -> int:
    """Return the first index where value > target."""
    start = 0
    end = len(arr)

    while start < end:
        mid = (start + end) // 2

        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1

    return start
