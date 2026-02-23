# Calculate the sum of Sub-Array Brute Force


# def max_sub_array_sum(arr, size):
#     max_sum = float("-inf")
#     for i in range(len(arr) - size + 1):
#         current_sum = 0
#         for j in range(i, i + size):
#             current_sum = current_sum + arr[j]
#         max_sum = max(max_sum, current_sum)
#     print(max_sum)
# max_sub_array_sum([2, 1, 5, 1, 3, 2], 3)


def max_sub_array_sum_sliding(arr, size):
    max_sum = float("-inf")
    current_max = 0

    if len(arr) < size:
        return None

    for i in range(size):
        current_max += arr[i]
    max_sum = current_max

    for j in range(size, len(arr)):
        current_max = current_max - arr[j - size] + arr[j]
        max_sum = max(current_max, max_sum)
    print(max_sum)


max_sub_array_sum_sliding([2, 1, 5, 1, 3, 2], 3)
