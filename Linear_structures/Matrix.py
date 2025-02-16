from typing import TypeVar, Optional, Iterable, Generic, Union, Tuple
from Vector import Vector
from Linear_Structure import Linear_Structure
import unittest

T = TypeVar('T')

class Matrix(Linear_Structure[T], Generic[T]):
    """
    Class for matrices.
    """
    
    def _init__(self, fill_val: Optional[T] = None, rows: Optional[int] = None , \
        cols: Optional[int] = None, elements: Optional[Iterable[Iterable[T]]] = None) -> None:
        
        if any(len(vec) != len(elements[0]) for vec in elements):
            raise ValueError('All rows must have the same length.')
        
        if elements is not None:
            self._matrix = [Vector(row) for row in elements]
            self.num_rows = len(elements)
            self.num_cols = len(elements[0])
            
        elif rows is not None and cols is not None:
            self._matrix = [Vector([fill_val]*cols) for _ in range(rows)]
            self.num_rows = rows
            self.num_cols = cols
        
        else:
            raise ValueError('You must provide either elements or rows and cols.')
        
    def append(self, vec: Vector[T]) -> None:
        if len(vec) != self.num_cols:
            raise ValueError('The vector must have the same length as the number of columns.')
        self._matrix.append(vec)
        self.num_rows += 1

    
    def pop(self) -> Vector[T]:
        return self._matrix.pop()
    
    def index(self, vec: Vector[T]) -> int:
        return self._matrix.index(vec)
    
    def insert(self, other: Union[Vector[T], "Matrix[T]"], axis: int = 0) -> None:
        """
        Concatenates another matrix or vector to this matrix.
        
        Parameters:
            other: Either a Vector (one row) or a Matrix.
            axis: 0 for vertical concatenation (adding rows),
                  1 for horizontal concatenation (adding columns).
        """
        if axis == 0:
            # Vertical concatenation: append rows.
            if isinstance(other, Vector):
                if len(other) != self.num_cols:
                    raise ValueError("The vector must have the same number of columns.")
                self.append(other)
                self.num_rows += 1
            elif isinstance(other, Matrix):
                if self.num_cols != other.num_cols:
                    raise ValueError("Matrices must have the same number of columns for vertical concatenation.")
                for row in other._matrix:
                    self._matrix.append(row)
                self.num_rows += other.num_rows
            else:
                raise TypeError("Other must be a Vector or Matrix.")
        
        elif axis == 1:
            # Horizontal concatenation: merge columns.
            if isinstance(other, Vector):
                # A one-dimensional vector can be interpreted as a column.
                if len(other) != self.num_rows:
                    raise ValueError("The vector must have the same number of rows for horizontal concatenation.")
                for i in range(self.num_rows):
                    self._matrix[i].append(other[i])
                self.num_cols += 1
            elif isinstance(other, Matrix):
                if self.num_rows != other.num_rows:
                    raise ValueError("Matrices must have the same number of rows for horizontal concatenation.")
                for i in range(self.num_rows):
                    # Append each element from the corresponding row of other.
                    for elem in other._matrix[i]:
                        self._matrix[i].append(elem)
                self.num_cols += other.num_cols
            else:
                raise TypeError("Other must be a Vector or Matrix.")
        
        else:
            raise ValueError("Axis must be 0 (vertical) or 1 (horizontal).")
        
    def __len__(self) -> Tuple[int, int]:
        return self.num_rows, self.num_cols