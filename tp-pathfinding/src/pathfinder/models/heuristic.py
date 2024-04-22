from ..models.grid import Grid


def heuristic(pos: tuple[int, int],) -> int:
    return abs(pos[0] - Grid.end[0]) + abs(pos[1] - Grid.end[1]) 