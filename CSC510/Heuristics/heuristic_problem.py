import heapq
import random

def heuristic_non_linear(current, goal):
    """A slightly less perfect heuristic to encourage exploration."""
    return abs(current - goal) + random.uniform(-2, 2)

def get_neighbors_non_linear(n):
    """More varied movement options."""
    neighbors = []
    neighbors.append(n + 1)
    neighbors.append(n - 1)
    neighbors.append(n + 2)
    neighbors.append(n - 2)
    if random.random() < 0.3:  # Introduce occasional larger jumps
        neighbors.append(n + 5)
    if random.random() < 0.3:
        neighbors.append(n - 5)
    return list(set(neighbors)) # Remove duplicates

def get_neighbors_non_linear_with_cost(n):
    """Varied movement costs."""
    neighbors = []
    neighbors.append((n + 1, 1))
    neighbors.append((n - 1, 1))
    neighbors.append((n + 2, 2))
    neighbors.append((n - 2, 2))
    if random.random() < 0.3:
        neighbors.append((n + 5, 3))
    if random.random() < 0.3:
        neighbors.append((n - 5, 3))
    return list(set(neighbors))

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def best_first_search(start, goal, get_neighbors, h):
    open_set = [(h(start, goal), start)]
    came_from = {}
    visited = {start}

    while open_set:
        priority, current = heapq.heappop(open_set)

        if current == goal:
            return came_from

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                heapq.heappush(open_set, (h(neighbor, goal), neighbor))

    return None

def greedy_best_first_search(start, goal, get_neighbors, h):
    open_set = [(h(start, goal), start)]
    came_from = {}
    visited = {start}

    while open_set:
        priority, current = heapq.heappop(open_set)

        if current == goal:
            return came_from

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                heapq.heappush(open_set, (h(neighbor, goal), neighbor))

    return None

def beam_search(start, goal, get_neighbors, h, beam_width=2):
    beam = [(h(start, goal), start)]
    visited = {start}

    while beam:
        new_beam = []
        beam.sort(key=lambda item: item[0])
        current_beam = beam[:beam_width]

        for priority, current in current_beam:
            if current == goal:
                return goal

            for neighbor in get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_beam.append((h(neighbor, goal), neighbor))

        beam = new_beam

    if beam:
        beam.sort(key=lambda item: item[0])
        return beam[0][1]
    return None

def a_star_search(start, goal, get_neighbors, h, cost_function):
    open_set = [(h(start, goal), 0, start)]  # f_score, g_score, state
    came_from = {}
    g_score = {start: 0}
    f_score = {start: h(start, goal)}

    while open_set:
        f, g, current = heapq.heappop(open_set)

        if current == goal:
            return came_from

        for neighbor, cost in get_neighbors(current):
            tentative_g_score = g_score[current] + cost
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], tentative_g_score, neighbor))

    return None

if __name__ == "__main__":
    while True:
        method_choice = input("\nChoose a search method (best-first, greedy, beam, a*, quit): ").lower()
        if method_choice == 'quit':
            break
        try:
            start_interactive = int(input("Enter the starting number: "))
            goal_interactive = int(input("Enter the goal number: "))

            if method_choice == 'best-first':
                path = best_first_search(start_interactive, goal_interactive, get_neighbors_non_linear, heuristic_non_linear)
                if path:
                    print("Best-First Search Path:", reconstruct_path(path, goal_interactive))
                else:
                    print("Best-First Search: No path found.")
            elif method_choice == 'greedy':
                path = greedy_best_first_search(start_interactive, goal_interactive, get_neighbors_non_linear, heuristic_non_linear)
                if path:
                    print("Greedy Best-First Search Path:", reconstruct_path(path, goal_interactive))
                else:
                    print("Greedy Best-First Search: No path found.")
            elif method_choice == 'beam':
                beam_width_interactive = int(input("Enter the beam width: "))
                result = beam_search(start_interactive, goal_interactive, get_neighbors_non_linear, heuristic_non_linear, beam_width_interactive)
                if isinstance(result, int):
                    print(f"Beam Search (width {beam_width_interactive}) Result (closest found):", result)
                elif result is not None:
                    print(f"Beam Search (width {beam_width_interactive}) Goal found:", result)
                else:
                    print(f"Beam Search (width {beam_width_interactive}): No solution found within the beam.")
            elif method_choice == 'a*':
                path = a_star_search(start_interactive, goal_interactive, get_neighbors_non_linear_with_cost, heuristic_non_linear, lambda a, b: 1 if abs(a - b) == 1 else 2 if abs(a - b) == 2 else 3 if abs(a - b) == 5 else 1)
                if path:
                    print("A* Search Path:", reconstruct_path(path, goal_interactive))
                else:
                    print("A* Search: No path found.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter numbers.")