"""Dijkstra algorithm implementation adapted for the SiMath project.

Provides: dijkstra(graph, start) -> (distances, previous_nodes)
and shortest_path(previous_nodes, start, target) -> list

When run as a script, the module loads `config.yaml` from the same
directory and prints the shortest distances and path.
"""

from typing import Dict, Tuple, Any, List
import heapq
import os
import yaml


def dijkstra(graph: Dict[Any, Dict[Any, float]], start: Any) -> Tuple[Dict[Any, float], Dict[Any, Any]]:
    """Compute shortest paths from `start` to all reachable nodes.

    Args:
        graph: adjacency mapping where graph[u][v] is the weight (numeric).
        start: starting node key.

    Returns:
        distances: mapping node -> shortest distance (float('inf') when unreachable).
        previous_nodes: mapping node -> previous node on shortest path (or None).
    """
    if start not in graph:
        raise KeyError(f"Start node {start!r} not found in graph")

    priority_queue: List[Tuple[float, Any]] = []
    heapq.heappush(priority_queue, (0.0, start))  # (cost, node)

    distances = {node: float('infinity') for node in graph}
    distances[start] = 0.0

    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.get(current_node, {}).items():
            try:
                w = float(weight)
            except Exception:
                raise ValueError(f"Edge weight for ({current_node}->{neighbor}) is not numeric: {weight!r}")

            distance = current_distance + w

            if distance < distances.get(neighbor, float('infinity')):
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes


def shortest_path(previous_nodes: Dict[Any, Any], start: Any, target: Any) -> List[Any]:
    """Reconstruct shortest path from start to target using previous_nodes.

    If the target is unreachable this returns an empty list.
    """
    if target not in previous_nodes:
        return []

    path = []
    node = target

    # Walk backwards until start or None encountered
    while node is not None:
        path.append(node)
        if node == start:
            break
        node = previous_nodes.get(node)

    if not path or path[-1] != start:
        # start not reached -> target unreachable
        return []

    path.reverse()
    return path


def load_config(path: str) -> Dict[str, Any]:
    """Load yaml config file with keys: graph, start, target, pretty_print (optional).

    The graph is expected to be a mapping of node -> mapping(neighbor -> weight).
    """
    with open(path, 'r') as f:
        cfg = yaml.safe_load(f) or {}

    return cfg


def main():
    # Locate config.yaml next to this file
    cfg_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    if not os.path.exists(cfg_path):
        print(f"Config file not found: {cfg_path}")
        return

    cfg = load_config(cfg_path)
    graph = cfg.get('graph', {})
    start = cfg.get('start')
    target = cfg.get('target')
    pretty = cfg.get('pretty_print', True)

    if start is None:
        print("'start' not set in config.yaml")
        return

    distances, previous = dijkstra(graph, start)

    if pretty:
        print("Shortest distances from start node:")
        for node, dist in distances.items():
            print(f"  {node}: {dist}")
    else:
        print(distances)

    if target is not None:
        path = shortest_path(previous, start, target)
        if path:
            print(f"Shortest path from {start} to {target}:", path)
        else:
            print(f"No path from {start} to {target} (target unreachable)")


if __name__ == '__main__':
    main()