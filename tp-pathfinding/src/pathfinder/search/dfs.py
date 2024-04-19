from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("",
                    grid.start,
                    0,
                    None,
                    None)

        # Add node to the expanded dictionary
        expanded = {}         
        
        # Return if the node contains a goal state
        if node.state == grid.end:
            return Solution(expanded)
        

        # Initialize the frontier with the initial node
        # The frontier is a stack
        frontier = StackFrontier()
        frontier.add(node)

        while True:

            # Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(expanded)
            
            # Remove a node from the frontier
            node = frontier.remove()

            # Discard node already expanded
            if node.state in expanded:
                continue

            # Mark the node as expanded
            expanded[node.state] = True

            # Generate all possible action and successor states
            successors = grid.get_neighbours(node.state)

            # For each succesor
            for action, state in successors.items():

                # Check if the successor is not expanded
                if state not in expanded:

                    # Initialize the son node
                    new_node = Node("",
                                    state,
                                    node.cost + grid.get_cost(state),
                                    node,
                                    action)
                    
                    # Return if the node contains a goal state
                    if new_node.state == grid.end:
                        return Solution(new_node,expanded)
                    
                    # Add new node to the frontier
                    frontier.add(new_node)

                    




            
