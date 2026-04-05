def linear_search(arr: list[int], target: int) -> int:
    """Return the index of target using linear search, or -1 if missing."""
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
