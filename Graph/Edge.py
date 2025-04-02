from typing import TypeVar, Generic, Optional, Tuple

E = TypeVar('E')  # Edge data type

class Edge(Generic[E]):
    """
    Represents an edge in a graph.
    """
    def __init__(self, source: Vertex, destination: Vertex, edge_data: Optional[E] = None) -> None:
        self._source = source
        self._destination = destination
        self._edge_data = edge_data

    def get_source(self) -> Vertex:
        return self._source

    def get_destination(self) -> Vertex:
        return self._destination

    def get_edge_data(self) -> Optional[E]:
        return self._edge_data

    def __str__(self) -> str:
        return f"Edge({self._source}, {self._destination}, {self._edge_data})"