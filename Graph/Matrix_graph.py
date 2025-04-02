from Graph.Graph import Graph
from typing import TypeVar, Generic, List, Optional, Tuple
from Linear_Structures.Matrix import Matrix
from Graph.Vertex import Vertex
from Graph.Edge import Edge
from Set.Vector_set import Vector_set

V = TypeVar('V')  # Vertex type
E = TypeVar('E')  # Edge data type


class MatrixGraph(Graph[V, E], Generic[V, E]):

    def __init__(self, other: Optional[Graph[V, E]] = None, directed: bool = False, weighted: bool = False) -> None:
        super().__init__(directed, weighted)
        self._matrix = Matrix[V, E]()
        self.vertices = set()
        if other:
            edges = other.get_edges()
            vertices = other.get_vertices()
            for vertex in vertices:
                self.add_vertex(vertex)
            for edge in edges:
                source, destination, edge_data = edge
                self.add_edge(source, destination, edge_data)

    def add_vertex(self, vertex: V) -> None:
        pass

    def remove_vertex(self, vertex: V) -> None:
        pass

    def add_edge(self, source: V, destination: V, edge_data: Optional[E] = None) -> None:
        pass

    def remove_edge(self, source: V, destination: V) -> None:
        pass

    def has_vertex(self, vertex: V) -> bool:
        pass

    def has_edge(self, source: V, destination: V) -> bool:
        pass

    def get_vertices(self) -> List[V]:
        pass

    def get_edges(self) -> List[Tuple[V, V, Optional[E]]]:
        pass

    def get_neighbors(self, vertex: V) -> List[Tuple[V, Optional[E]]]:
        pass

    def get_edge_data(self, source: V, destination: V) -> Optional[E]:
        pass

    def is_directed(self) -> bool:
        pass

    def __len__(self) -> int:
        pass

    def dfs(self, start: V) -> List[V]:
        pass

    def bfs(self, start: V) -> List[V]:
        pass
