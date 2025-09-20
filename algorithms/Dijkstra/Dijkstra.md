# Dijkstra's Algorithm

## Mathematical Background

Dijkstra's algorithm finds the shortest paths from a single source node to all
other nodes in a weighted graph with non-negative edge weights. It is a greedy
algorithm that repeatedly selects the closest unvisited node and relaxes its
outgoing edges.

## Algorithm Description

1. Initialize distances to +infinity for all nodes except the start node (0).
2. Use a priority queue (min-heap) keyed by distance.
3. Pop the node with smallest tentative distance.
4. For each outgoing edge, compute new tentative distance and update if
   smaller.
5. Repeat until the queue is empty.

Time complexity (using binary heap): O((V + E) log V).

## Code Overview

The package exports two main functions:

- `dijkstra(graph, start)` – returns `(distances, previous_nodes)` where
  distances is a mapping node->float and previous_nodes can be used to
  reconstruct shortest paths.
- `shortest_path(previous_nodes, start, target)` – returns ordered list of
  nodes from start to target, or an empty list if unreachable.

The module also provides a `main()` which loads `config.yaml` next to the
module and prints distances and an example path.

### Expected config.yaml keys

- `graph`: mapping node -> mapping(neighbor -> numeric weight)
- `start`: start node key
- `target`: (optional) target node key to print single path
- `pretty_print`: (optional) boolean to print user-friendly output

## Example usage

Run on Linux:

```bash
bash simulations/linux/Dijkstra.bash
```

Python usage from code:

```python
from simath.algorithms.Dijkstra.Dijkstra import dijkstra, shortest_path

graph = {...}
distances, prev = dijkstra(graph, 'A')
path = shortest_path(prev, 'A', 'D')
```

## Educational value

This implementation is compact and robust: it validates numeric weights and
returns unreachable nodes with infinite distance. Use it to teach greedy
algorithms, priority queues, and path reconstruction.
