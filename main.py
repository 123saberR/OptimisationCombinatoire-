cities = [
    [0, 61, 63, 144, 128, 0, 0, 0, 0],
    [61, 0, 0, 94, 0, 0, 0, 0, 0],
    [63, 0, 0, 0, 70, 168, 0, 0, 0],
    [144, 94, 0, 0, 82, 122, 0, 225, 0],
    [128, 0, 70, 82, 0, 130, 0, 146, 0],
    [0, 0, 168, 122, 130, 0, 39, 148, 523],
    [0, 0, 0, 0, 0, 39, 0, 201, 0],
    [0, 0, 0, 225, 146, 148, 201, 0, 331],
    [475, 0, 0, 0, 0, 523, 0, 331, 0]
]

cities_name = ["Tétouan", "Tanger", "Chefchaouen", "Larache", "Ouazzane", "Kenitra", "Rabat", "FES", "OUJDA"]


def PPV_TSP(cities, start):
    visited = [False] * len(cities)
    path = [start]
    total_distance = 0
    current_city = start
    visited[start] = True

    for _ in range(len(cities) - 1):
        neighbors = cities[current_city]
        nearest_city = None
        min_distance = float('inf')

        for city, distance in enumerate(neighbors): # [128, 0, 70, 82, 0, 130, 0, 146, 0]
            if not visited[city] and distance < min_distance and distance > 0:
                nearest_city = city
                min_distance = distance
        # print(nearest_city, min_distance)

        path.append(nearest_city)
        if nearest_city is not None:
            visited[nearest_city] = True
            total_distance += min_distance
            current_city = nearest_city
        else:
            return path, total_distance


    if cities[current_city][start] > 0:
        total_distance += cities[current_city][start]
        path.append(start)

    return path, total_distance

print(PPV_TSP(cities, start=4))
