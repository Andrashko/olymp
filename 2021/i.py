from math import inf

# Алгоритм Прима
def prima(distance_matrix):
    cities_count = len(distance_matrix)
    free_vertexes = set(range(1, cities_count))
    tied = set([0])
    road_length = 0

    while len(free_vertexes) > 0:
        min_link = None
        overall_min_path = inf

        for current_vertex in tied:
            weights = distance_matrix[current_vertex]

            min_path = inf
            free_vertex_min = current_vertex

            for vertex in range(cities_count):
                vertex_path = weights[vertex]

                if vertex in free_vertexes and vertex_path < min_path:
                    free_vertex_min = vertex
                    min_path = vertex_path

            if free_vertex_min != current_vertex:
                if overall_min_path > min_path:
                    min_link = (current_vertex, free_vertex_min)
                    overall_min_path = min_path
        path_length = distance_matrix[min_link[0]][min_link[1]]

        road_length += path_length
        free_vertexes.remove(min_link[1])
        tied.add(min_link[1])

    return road_length


n, M = list(map(int, input().split()))
a = list(map(int, input().split()))

distance_matrix = []
for ai in a:
    row = []
    for aj in a:
        row.append((ai+aj) % M)
    distance_matrix.append(row)

print(prima(distance_matrix))
