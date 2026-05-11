import collections
import heapq

def find_smart_path(grid_width, grid_height, food_points, initial_len=3, max_len=30):
    """
    Intelligent hunting algorithm: Shortest path to clusters with survival checks.
    """
    food_set = set(food_points)
    
    def get_a_star_path(start, target, body):
        # body is a list of coordinates
        body_set = set(body)
        # Priority Queue: (priority, current_pos, path)
        # Priority = cost_so_far + heuristic(pos, target)
        pq = [(0, start, [])]
        visited = {start: 0}
        
        while pq:
            cost, (cx, cy), path = heapq.heappop(pq)
            if (cx, cy) == target: return path
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < grid_width and 0 <= ny < grid_height:
                    # Check if cell is occupied by body
                    # Note: tail will move, but for simplicity we treat body as static during A*
                    if (nx, ny) not in body_set:
                        new_cost = cost + 1
                        if (nx, ny) not in visited or new_cost < visited[(nx, ny)]:
                            visited[(nx, ny)] = new_cost
                            priority = new_cost + abs(nx - target[0]) + abs(ny - target[1])
                            heapq.heappush(pq, (priority, (nx, ny), path + [(nx, ny)]))
        return None

    def can_survive(pos, body):
        # Check if snake can reach its own tail (classic survival check)
        if not body: return True
        tail = body[-1]
        # BFS to see if tail is reachable from new pos
        queue = collections.deque([pos])
        visited = {pos} | set(list(body)[:-1]) # Tail is considered 'free' soon
        reachable_count = 0
        while queue:
            cp = queue.popleft()
            reachable_count += 1
            if cp == tail or reachable_count > 50: return True
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                np = (cp[0]+dx, cp[1]+dy)
                if 0 <= np[0] < grid_width and 0 <= np[1] < grid_height and np not in visited:
                    visited.add(np)
                    queue.append(np)
        return False

    current_pos = (0, 0)
    snake_body = collections.deque([current_pos] * initial_len, maxlen=max_len)
    full_path = [current_pos]
    targets = list(food_points)
    eaten_indices = []
    
    print(f"--- SMART HUNTING START ---")
    
    while targets:
        # Find the best target: nearest that is SURVIVABLE
        targets.sort(key=lambda t: abs(t[0]-current_pos[0]) + abs(t[1]-current_pos[1]))
        
        best_path = None
        chosen_target = None
        
        for t in targets[:5]: # Check 5 nearest targets
            path = get_a_star_path(current_pos, t, snake_body)
            if path:
                # Tentatively check if the last step is survivable
                if can_survive(path[-1], snake_body):
                    best_path = path
                    chosen_target = t
                    break
        
        if not best_path:
            # Survival mode: move towards a point that has most free space
            moved = False
            # Try to move towards the furthest free neighbor
            neighbors = []
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = current_pos[0]+dx, current_pos[1]+dy
                if 0 <= nx < grid_width and 0 <= ny < grid_height and (nx, ny) not in set(snake_body):
                    neighbors.append((nx, ny))
            
            if neighbors:
                # Choose neighbor with most reachable space
                next_move = max(neighbors, key=lambda n: len(get_a_star_path(n, (grid_width-1, grid_height-1), snake_body) or []))
                best_path = [next_move]
            else:
                print("Game Over: No moves left!")
                break
        
        # Execute the path
        for move in best_path:
            current_pos = move
            full_path.append(current_pos)
            if chosen_target and current_pos == chosen_target:
                targets.remove(chosen_target)
                eaten_indices.append(len(full_path) - 1)
                print(f"Hunted {chosen_target}! Length: {len(snake_body)}")
                if len(snake_body) >= max_len: snake_body.pop()
            else:
                snake_body.pop()
            snake_body.appendleft(current_pos)
            
    print(f"Simulation complete. Steps: {len(full_path)}")
    return full_path, eaten_indices

if __name__ == "__main__":
    test_food = [(1, 1), (5, 5), (10, 2), (2, 6), (15, 3), (20, 0)]
    path, eaten = find_smart_path(52, 7, test_food)
    print(f"Eaten at steps: {eaten}")
