import numpy as np
import copy

def play_step(world, neighbors, pt2):
    next_world = copy.deepcopy(world)
    for y in range(len(world)):
        for x in range(len(world[y])):

            cell = world[y][x]
            neighbor_count = 0
            # Getting neighbors (3x3 grid skipping center)
            for yy in [-1, 0, 1]:
                for xx in [-1, 0, 1]:
                    if yy == 0 and xx == 0:
                        continue

                    y_cell = y+yy
                    x_cell = x+xx
                    if pt2:
                        # Checking neighbors are all valid (and not beyond the bounds of the edges)
                        edges = (y_cell >= 0 and x_cell >= 0)
                        bounds = (y_cell < len(world) and x_cell < len(world[y]))
                        while edges and bounds and world[y_cell][x_cell] == '.':
                            y_cell += yy
                            x_cell += xx
                            edges = (y_cell >= 0 and x_cell >= 0)
                            bounds = (y_cell < len(world) and x_cell < len(world[y]))
                        if edges and bounds and world[y_cell][x_cell] == '#':
                            neighbor_count += 1

                    else:
                        # Checking neighbors are all valid (and not beyond the bounds of the edges)
                        if (y_cell >= 0 and x_cell >= 0) and (y_cell < len(world) and x_cell < len(world[y])):
                            neighbor = world[y_cell][x_cell]
                            # check if neighbor is alive
                            if neighbor == "#":
                                neighbor_count += 1
            # cell is alive
            if cell == '#' and neighbor_count > neighbors:
                next_world[y][x] = 'L'
            # If cell is dead
            elif cell == 'L' and neighbor_count == 0:
                next_world[y][x] = '#'
    return next_world

def compare_grids(prevgrid, neighbors, pt2):
    aftgrid = play_step(prevgrid, neighbors, pt2)
    while prevgrid != aftgrid:
        prevgrid = aftgrid
        aftgrid = play_step(prevgrid, neighbors, pt2)
        #print(aftgrid)
    count = 0
    for line in aftgrid:
        for cell in line:
            if '#' == cell:
                count += 1
    return count


with open('input.txt') as f:
    grid = [[square for square in line] for line in f.read().split('\n')]

# sol1: 2277
print(compare_grids(grid, 3, False))
print(compare_grids(grid, 4, True))
