from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

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

        # Add the node to the explored dictionary
        explored = {} 
        explored[node.state] = True

        # Return if the node contains a goal state
        if node.state == grid.end:
            return Solution(node,explored)

        
        # Initialize the frontier with the initial node
        # The frontier is a queue
        frontier = QueueFrontier()
        frontier.add(node)
        
        while True:

            #  Fail if the frontier is empty
            if frontier.is_empty:
                return NoSolution(explored)
            
            # Remove a node from the frontier
            node=frontier.remove()

            # Generate all possible action and successor states
            successors = grid.get_neighbours(node.state)

            # For each successor
            for action, state in successors.items():


                # Check if the successor is not explored
                if state not in explored:
                    
                    # Initialize the son node
                    new_node= Node("",
                                   state, 
                                   node.cost + grid.get_cost(state),
                                   node,
                                   action)
                    
                    # Mark the successor as explored
                    explored[state] = True
                    
                    # Return if the node contains a goal state
                    if state == grid.end:
                        return Solution(new_node,explored)

                    # Add new node to the frontier
                    frontier.add(new_node)

