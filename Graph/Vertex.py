from typing import TypeVar, Generic, Optional, Tuple

from Linear_Structures.Vector import Vector

V = TypeVar('V')  # Vertex type


class Vertex(Generic[V]):
    """
    Represents a vertex in a graph.
    """

    def __init__(self, label: V) -> None:
        self._label = label
        self._neighbors: Vector[V] = Vector()
        self._visited = False

    def __str__(self):
        return str(self._label)

    def __eq__(self, other) -> bool:
        if isinstance(other, Vertex):
            return self._label == other._label and self._neighbors == other._neighbors
        return False
