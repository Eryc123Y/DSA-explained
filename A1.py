"""
Author: Xingyu Yang 33533563
Data: 2025-04-xx
"""
from typing import List, Tuple

# Utility functions for problem-solving

def generate_adjacency_list(roads: List[Tuple[int, int, int, int]]) -> List[List]:
    """
    Generate an adjacency list from the given list of roads.
    """
    adjacency_list = []
    for road in roads:
        a, b, c, d = road
        if a >= len(adjacency_list):
            adjacency_list.extend([[] for _ in range(a - len(adjacency_list) + 1)])
        if b >= len(adjacency_list):
            adjacency_list.extend([[] for _ in range(b - len(adjacency_list) + 1)])
        adjacency_list[a].append((b, c, d))
        adjacency_list[b].append((a, c, d))
    return adjacency_list

def display_adjacency_list(adj_list: List[List]) -> str:
    """A auxiliary function to display the adjacency list in a readable format

    Args:
        adj_list (List[List]): The adjacency list to be displayed

    Returns:
        str: The string representation of the adjacency list
    """
    result = ""
    for i, adj in enumerate(adj_list):
        result += f"{i}: {adj}\n"
    return result

def is_station(stations: List[Tuple[int, int]], node: int) -> bool:


def main():
    roads_example1 = [(6,0,3,1), (6,7,4,3), (6,5,6,2), (5,7,10,5), (4,8,8,5), (5,4,8,2),
(8,9,1,2), (7,8,1,3), (8,3,2,3), (1,10,5,4), (0,1,10,3), (10,2,7,2),
(3,2,15,2), (9,3,2,2), (2,4,10,5)]
    stations_example1 = [(0,1), (5,1), (4,1), (3,1), (2,1), (1,1)]
    adj_list1 = generate_adjacency_list(roads_example1)
    print(display_adjacency_list(adj_list1))
    
    
if __name__ == "__main__":
    main()