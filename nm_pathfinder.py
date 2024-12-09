import math
from queue import PriorityQueue

def find_box_containing_point(boxes, point):
    y, x = point
    for box in boxes:
        y1, y2, x1, x2 = box
        if x1 <= x <= x2 and y1 <= y <= y2:
            return box
    return None

def euclidean_distance(point1, point2):
    y1, x1 = point1
    y2, x2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def a_star_search(mesh, start_box, goal_box, start_point, goal_point):
    frontier = PriorityQueue()

    forward_prev = {start_box: []}          # maps cells to previous cells on path
    backward_prev = {goal_box: []}
    forward_dist = {start_box: 0}       # maps cells to their path costs (found so far)
    backward_dist = {goal_box: 0}
    detail_points = {start_box: start_point, goal_box: goal_point}  # track detailed points

    frontier.put((0, start_box, 'forward'))
    frontier.put((0, goal_box, 'backward'))
    common_node = None
    

    while not frontier.empty():
        priority, current_box, direction = frontier.get()

        if direction == 'forward':
            if current_box in backward_prev:
                common_node = current_box
                break
        elif direction == 'backward':
            if current_box in forward_prev:
                common_node = current_box
                break

        for next_box in mesh['adj'][current_box]:
            
            # Check if next_box is in forward_prev to find common node
            y1, y2, x1, x2 = next_box
            current_point = detail_points[current_box]
            next_point = (
                min(max(current_point[0], y1), y2),
                min(max(current_point[1], x1), x2)
            )
            
            if direction == 'forward':
                new_cost = forward_dist[current_box] + euclidean_distance(current_point, next_point)
                if next_box not in forward_dist or new_cost < forward_dist[next_box]:
                    forward_dist[next_box] = new_cost
                    priority = new_cost + euclidean_distance(goal_point, next_point)
                    frontier.put((priority, next_box, 'forward'))
                    forward_prev[next_box] = current_box
                    detail_points[next_box] = next_point

                    # Check if next_box is in backward_prev to find common node
                    if next_box in backward_prev:
                        common_node = next_box
                        break
                
            elif direction == 'backward':
                new_cost = backward_dist[current_box] + euclidean_distance(current_point, next_point)
                if next_box not in backward_dist or new_cost < backward_dist[next_box]:
                    backward_dist[next_box] = new_cost
                    priority = new_cost + euclidean_distance(start_point, next_point)
                    frontier.put((priority, next_box, 'backward'))
                    backward_prev[next_box] = current_box
                    detail_points[next_box] = next_point

                                
                    # Check if next_box is in forward_prev to find common node
                    if next_box in forward_prev:         
                        common_node = next_box
                        break

    # If no common node found, return no path
    if common_node is None :
        print("No path found!")
        return [], [], [], []
    
    

    return forward_prev, backward_prev, detail_points, common_node

def reconstruct_path(forward_prev, backward_prev, detail_points, meeting_node, start_box, goal_box):
    path = []

    # Reconstruct path from start_box to meeting_node
    current = meeting_node
    while current != start_box:
        path.append(detail_points[current])
        current = forward_prev[current]
    path.reverse()

    # Reconstruct path from meeting_node to goal_box
    current = meeting_node
    while current != goal_box:
        path.append(detail_points[current])
        current = backward_prev[current]
    path.append(detail_points[goal_box])

    return path

def find_path(source_point, destination_point, mesh):

    start_box = find_box_containing_point(mesh['boxes'], source_point)
    goal_box = find_box_containing_point(mesh['boxes'], destination_point) 



    # draw straight line if in same box
    if start_box == goal_box:
        return [source_point, destination_point], [start_box]
    
    if not start_box or not goal_box:
        return [], []

    forward_prev, backward_prev, detail_points, common_node = a_star_search(mesh, start_box, goal_box, source_point, destination_point)

    if not forward_prev or not backward_prev:
        return [], []
    
    path = reconstruct_path(forward_prev, backward_prev, detail_points, common_node, start_box, goal_box)

    if source_point not in path: 
        path.insert(0,source_point)
    return path, list(forward_prev.keys()) + list(backward_prev.keys())