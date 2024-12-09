# Leonardo Dulanto

## Workflow 1

The following steps outline a straightforward approach to implementing and refining a pathfinding algorithm within a grid or graph structure. This process focuses on identifying key locations (source and destination), using the Breadth-First Search (BFS) algorithm for initial path discovery, enhancing BFS to record more detailed traversal information, and finally translating those findings into a clear set of legal line segments.

### Steps

1. **Identify the Source and Destination Boxes**  
   Begin by pinpointing the exact start (source) and end (destination) nodes or cells in the given environment. These could be specific coordinates in a grid, nodes in a graph, or marked positions in a dataset. This step provides the reference points from which the search will originate and terminate.

2. **Implement the Simplest Complete Search Algorithm (BFS)**  
   Start with a basic, unoptimized BFS. BFS ensures that once you find the destination, you've discovered the shortest possible path in terms of edge count. At this stage:
   - Initialize a queue with the source node.
   - Explore neighbors level-by-level until you find the destination.
   - Keep track of visited nodes to prevent cycles and repetition.
   
   The output of this step should be a path from the source to the destination, if one exists.

3. **Modify BFS to Track Detailed Points**  
   Enhance the BFS to record more than just the visited state of each node. For example:
   - Store parent pointers or references to the node from which you arrived at the current node. This allows you to reconstruct the exact path once the destination is reached.
   - Track additional data such as distances, the sequence of visited nodes, or any special conditions required by the problem (e.g., costs, constraints).
   
   After this modification, your BFS should produce a rich data structure that fully describes the discovered path and its characteristics.

4. **Construct a Legal List of Line Segments**  
   Using the detailed path information from the modified BFS, generate a sequence of line segments that connect each consecutive pair of points along the path. These segments represent the final, legal moves from the start to the destination. For example:
   - Extract the path from the destination node by following parent pointers back to the source.
   - Convert each pair of adjacent nodes in the path into a line segment (e.g., `(x1, y1) -> (x2, y2)`).
   - Validate that each segment adheres to any defined constraints (e.g., not crossing obstacles, remaining within specified boundaries).
   
   The resulting list of line segments provides a clean, geometric representation of the solution path suitable for visualization, further analysis, or integration into additional systems.

---

**In summary**, this workflow starts with the foundational BFS algorithm to find a path, then refines the solution to produce a detailed and geometrically meaningful representation of the discovered route. The final output—a list of legal line segments—can be invaluable for rendering, simulating, or reasoning about the path in more complex applications.
