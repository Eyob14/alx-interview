#!/usr/bin/python3
"""
    This file contains the island_perimeter function that calculates
    the perimeter of the island in the given grid
    """


def dfs(i, j, grid, visited):
    """
    This function runs dfs on the grid
    """
    if (
        i < 0 or j < 0 or
        i >= len(grid) or
        j >= len(grid[0]) or
        grid[i][j] == 0
    ):
        return 1
    if (i, j) in visited:
        return 0

    visited.add((i, j))
    perimeter = dfs(i, j+1, grid, visited)
    perimeter += dfs(i+1, j, grid, visited)
    perimeter += dfs(i, j-1, grid, visited)
    perimeter += dfs(i-1, j, grid, visited)

    return perimeter


def island_perimeter(grid):
    """
    This function calculates the perimeter of the island in the given grid.
    """
    visited = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return dfs(i, j, grid, visited)
