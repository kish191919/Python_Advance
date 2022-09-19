
def grid_info(grid):
    # Finding grid boundaries
    max_row = len(grid)
    max_col = len(grid[0])

    # The number 1 means the building, so the sum of 1 is equal to the sum of the buildings
    total_buildings = sum([col for row in grid for col in row if col == 1])

    # Initialize distance and need_visit
    need_visit = [[0]*max_col for _ in range(max_row)]
    distances = [[0]*max_col for _ in range(max_row)]
    return max_row, max_col, total_buildings, need_visit, distances


def calculate_distance(row, col, max_row, max_col, need_visit, distances,grid):
    # Start at the building location. That's why building_count is 1
    building_count = 1

    # grid cells already visited
    visited = {(row, col)}

    # queue = [(row, col, distance)]
    queue = [(row, col, 0)]

    # The loop is executed until there is no more need_visit in the queue
    while queue:
        q_row, q_col, distance = queue.pop(0)

        # Execute a loop statement while moving up, down, right, and left
        for next_row, next_col in [(q_row+1, q_col), (q_row-1, q_col), (q_row, q_col+1), (q_row, q_col-1)]:

            # Execute if the movement is within the grid's bounds, greater than 0, and a grid position that has never been calculated.
            if (0 <= next_row < max_row) and (0 <= next_col < max_col) and (next_row, next_col) not in visited:
                visited.add((next_row, next_col))

                # In cae of an empty land
                if grid[next_row][next_col] == 0:

                    # It is stored in the queue and later run in a loop to calculate distance
                    queue.append((next_row, next_col, distance+1))

                    # Increment 1 for each visit, later this number must equal the total number of buildings
                    need_visit[next_row][next_col] += 1

                    # The distance from the building, incremented by 1.
                    distances[next_row][next_col] += distance+1

                # If there is a 1 on the grid, it counts the number of buildings.
                if grid[next_row][next_col] == 1:
                    building_count += 1

    return building_count, distances, need_visit


def main(grid):
    # Get necessary information through grid_info function
    max_row, max_col, total_buildings, need_visit, distances = grid_info(grid)

    for row in range(max_row):
        for col in range(max_col):

            # Calculate distance from buildings
            # buildings are located at 1
            if grid[row][col] == 1:

                # Calculate the distance
                building_count, distances, need_visit = calculate_distance(row,col,max_row, max_col,need_visit,distances,grid)

    # Find the minimum of non-zero distance values
    min_distance = [distance for rows in zip(distances, need_visit) for distance, building_visit_count in zip(*rows) if distance !=0 and building_visit_count == total_buildings]

    if min_distance:
        return min(min_distance)
    else:
        return -1

if __name__=="__main__":
    # First example
    grid_1 = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    print("First example")
    print("Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]")
    print("Output: ", main(grid_1))
    print("*" * 20)

    # Second example
    grid_2 = [[1,0]]
    print("Second example")
    print("Input: grid = [[1,0]]")
    print("Output: ",main(grid_2))
    print("*" * 20)

    # Third example
    print("Third example")
    print("Input: grid = [[1]]")
    grid_3 = [[1]]
    print("Output: ",main(grid_3))



