def sliding_window(num_list, k):
    if k <= 0:
        return []

    n = len(num_list)
    max_list = []

    for i in range(n - k + 1):
        current_window_max = max(num_list[i:i + k])
        max_list.append(current_window_max)

    return max_list


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3

max_value = sliding_window(num_list, k)
print(f'Output: {max_value}')
