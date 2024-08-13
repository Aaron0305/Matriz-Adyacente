# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 22:45:03 2023

@author: DELL
"""
import heapq

def dijkstra(graph, start):
    if start not in graph:
        raise ValueError("El nodo de inicio no está en el grafo")

    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 8, 'D': 5, 'E': 4},
    'B': {'A': 8, 'C': 3, 'F': 4},
    'C': {'B': 3, 'F': 9, 'G': 11},
    'D': {'A': 5, 'E': 9, 'H': 6},
    'E': {'A': 4, 'D': 9, 'F': 3, 'I': 8, 'J': 5},
    'F': {'B': 4, 'C': 9, 'E': 3, 'G': 1, 'K': 8},
    'G': {'C': 11, 'F': 1, 'K': 8, 'L': 7},
    'H': {'D': 6, 'I': 2, 'M': 7},
    'I': {'E': 8, 'H': 2, 'J': 10, 'M': 6},
    'J': {'E': 5, 'I': 10, 'K': 6, 'N': 9},
    'K': {'F': 8, 'G': 8, 'J': 6, 'L': 5, 'P': 7},
    'L': {'G': 7, 'K': 5, 'P': 6, 'Q': 7},
    'M': {'H': 7, 'I': 6, 'N': 2},
    'N': {'J': 9, 'M': 2, 'O': 8, 'P': 12, 'R': 3},
    'O': {'N': 8, 'P': 7, 'Q': 5, 'R': 3, 'S': 2},
    'P': {'K': 7, 'L': 6, 'N': 12, 'O': 7, 'Q': 2},
    'Q': {'L': 7, 'O': 5, 'P': 2, 'S': 7},
    'R': {'M': 3, 'N': 3, 'S': 9},
    'S': {'O': 2, 'Q': 7, 'R': 9},
}

start_node = 'A'

try:
    result = dijkstra(graph, start_node)
    for node, distance in result.items():
        print(f"Distancia de {start_node} a {node} = {distance}")
except ValueError as e:
    print(f"Error: {e}")
