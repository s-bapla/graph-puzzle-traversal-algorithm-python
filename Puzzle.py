import heapq

def solve_puzzle(Board, Source, Destination):
    queue = []
    heapq.heappush(queue, (0, Source))
    visited = set([Source])
    distance = {Source: 0}
    parent = {Source: None}

    while queue:
        current_cell = heapq.heappop(queue)
        if current_cell[1] == Destination:
            break

        row, col = current_cell[1]
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for neighbor in neighbors:
            if neighbor in visited or not is_valid_helper(Board, neighbor):
                continue
            visited.add(neighbor)
            new_distance = distance[current_cell[1]] + 1
            if neighbor not in distance or new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                parent[neighbor] = current_cell[1]
                priority = new_distance
                heapq.heappush(queue, (priority, neighbor))

    if Destination not in visited:
        return None

    path = []
    current_cell = Destination
    while current_cell is not None:
        path.append(current_cell)
        current_cell = parent[current_cell]
    path.reverse()

    return path, get_directions_helper(path)

def is_valid_helper(puzzle, cell):
    row, col = cell
    if row < 0 or col < 0 or row >= len(puzzle) or col >= len(puzzle[0]):
        return False
    if puzzle[row][col] == '#':
        return False
    return True

def get_directions_helper(path):
    directions = ''
    for i in range(1, len(path)):
        row_diff = path[i][0] - path[i-1][0]
        col_diff = path[i][1] - path[i-1][1]
        if row_diff == -1:
            directions += 'U'
        elif row_diff == 1:
            directions += 'D'
        elif col_diff == -1:
            directions += 'L'
        elif col_diff == 1:
            directions += 'R'
    return directions

