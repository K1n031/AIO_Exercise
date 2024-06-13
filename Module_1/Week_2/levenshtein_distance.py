def levenshtein_distance(source, target):
    len_source, len_target = len(source), len(target)

    distance_matrix = [[0 for _ in range(len_target + 1)]
                       for _ in range(len_source + 1)]

    for row in range(len_source + 1):
        distance_matrix[row][0] = row
    for col in range(len_target + 1):
        distance_matrix[0][col] = col

    for row in range(1, len_source + 1):
        for col in range(1, len_target + 1):
            cost = 0 if source[row - 1] == target[col - 1] else 1

            distance_matrix[row][col] = min(distance_matrix[row - 1][col] + 1,
                                            distance_matrix[row][col - 1] + 1,
                                            distance_matrix[row - 1][col - 1] + cost)

    return distance_matrix[len_source][len_target]


source = "kitten"
target = "sitting"
print(f"Levenshtein distance of '{source}' and '{
      target}' is: {levenshtein_distance(source, target)}")
