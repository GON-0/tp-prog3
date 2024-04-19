from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

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
        explored[node.state] = node.cost

        
        # Initialize the frontier with the initial node
        # The frontier is a priority queue
        frontier = PriorityQueueFrontier()
        frontier.add(node)

        while True:

            #  Fail if the frontier is empty
            if frontier.is_empty:
                return NoSolution(explored)
            
            # Remove a node from the frontier
            node = frontier.pop()

            # Return if the node contains a goal state
            if node.state == grid.end:
                return Solution(node,explored)
            
            # Generate all possible action and successor states
            successors = grid.get_neighbours(node.state)

            # For each successor
            for action, state in successors.items():

                # Initialize the new cost
                new_cost = node.cost + grid.get_cost(state)

                # Check if the successor is not explored or new_cost is lower 
                if state not in explored or new_cost < explored[state]:

                    # Initialize the son node
                    new_node = Node("",
                                    state,
                                    new_cost,
                                    node,
                                    action)
                    
                    # Mark the successor as explored
                    explored[state] = new_cost

                    # Add new node to the frontier
                    frontier.add(new_node, new_cost)
                    
                




            
            


