from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Iterator, List, Optional, Tuple, Set

V = TypeVar('V')  # Vertex type
E = TypeVar('E')  # Edge data type


class Graph(ABC, Generic[V, E]):
    """
    Abstract class for graphs.
    """
    def __init__(self, directed: bool = False, weighted:bool = False) -> None:
        self._num_vertices = 0
        self._num_edges = 0
        self._directed = directed
        self._weighted = weighted

    @abstractmethod
    def add_vertex(self, vertex: V) -> None:
        """
        Adds a vertex to the graph.
        """
        pass

    @abstractmethod
    def remove_vertex(self, vertex: V) -> None:
        """
        Removes a vertex from the graph.
        """
        pass

    @abstractmethod
    def add_edge(self, source: V, destination: V, edge_data: Optional[E] = None) -> None:
        """
        Adds an edge from source to destination.
        For undirected graphs, also adds an edge from destination to source.
        """
        pass

    @abstractmethod
    def remove_edge(self, source: V, destination: V) -> None:
        """
        Removes the edge from source to destination.
        For undirected graphs, also removes the edge from destination to source.
        """
        pass

    @abstractmethod
    def has_vertex(self, vertex: V) -> bool:
        """
        Returns True if the vertex exists in the graph.
        """
        pass

    @abstractmethod
    def has_edge(self, source: V, destination: V) -> bool:
        """
        Returns True if an edge exists from source to destination.
        """
        pass

    @abstractmethod
    def get_vertices(self) -> List[V]:
        """
        Returns a list of all vertices in the graph.
        """
        pass

    @abstractmethod
    def get_neighbors(self, vertex: V) -> List[Tuple[V, Optional[E]]]:
        """
        Returns a list of (neighbor, edge_data) tuples for the given vertex.
        """
        pass

    @abstractmethod
    def get_edge_data(self, source: V, destination: V) -> Optional[E]:
        """
        Returns the data associated with the edge from source to destination,
        or None if there is no such edge.
        """
        pass

    @abstractmethod
    def is_directed(self) -> bool:
        """
        Returns True if the graph is directed, False otherwise.
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """
        Returns the number of vertices in the graph.
        """
        pass

    @abstractmethod
    def dfs(self, start: V) -> List[V]:
        """
        Performs a depth-first search starting from the given vertex.
        Returns a list of vertices in the order they were visited.
        """
        pass

    @abstractmethod
    def bfs(self, start: V) -> List[V]:
        """
        Performs a breadth-first search starting from the given vertex.
        Returns a list of vertices in the order they were visited.
        """
        pass

    def count_edges(self) -> int:
        """
        Returns the number of edges in the graph.
        """
        return self._num_edges

    def count_vertices(self) -> int:
        """
        Returns the number of vertices in the graph.
        """
        return self._num_vertices

    def is_directed(self) -> bool:
        """
        Returns True if the graph is directed, False otherwise.
        """
        return self._directed

    def is_weighted(self) -> bool:
        """
        Returns True if the graph is weighted, False otherwise.
        """
        return self._weighted

    @abstractmethod
    def get_edges(self) -> List[Tuple[V, V, Optional[E]]]:
        """
        Returns a list of all edges in the graph.
        """
        pass
