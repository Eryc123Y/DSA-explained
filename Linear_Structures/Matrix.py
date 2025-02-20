from typing import TypeVar, Optional, Iterable, Generic, Union, Tuple
from Vector import Vector
from Linear_Structure import Linear_structure
import unittest

T = TypeVar('T')


class Matrix(Linear_structure[T], Generic[T]):
    """
    Class for matrices.
    """

    def __init__(self, fill_val: Optional[T] = None, rows: Optional[int] = None,
                 cols: Optional[int] = None, elements: Optional[Iterable[Iterable[T]]] = None) -> None:

        if any(len(vec) != len(elements[0]) for vec in elements):
            raise ValueError('All rows must have the same length.')

        if elements is not None:
            self._matrix = [Vector(row) for row in elements]
            self.num_rows = len(elements)
            self.num_cols = len(elements[0])

        elif rows is not None and cols is not None:
            self._matrix = [Vector([fill_val] * cols) for _ in range(rows)]
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

    def __len__(self) -> int:
        return self.num_rows

    @property
    def dims(self) -> Tuple[int, int]:
        return self.num_rows, self.num_cols

    def __getitem__(self, index: Union[int, Tuple[int, int]]) -> Union[Vector[T], T]:
        if isinstance(index, int):
            return self._matrix[index]
        elif isinstance(index, tuple):
            return self._matrix[index[0]][index[1]]
        else:
            raise TypeError("Index must be an integer or a tuple of integers.")

    def __setitem__(self, index: Union[int, Tuple[int, int]], value: Union[Vector[T], T]) -> None:
        if isinstance(index, int):
            self._matrix[index] = value
        elif isinstance(index, tuple):
            self._matrix[index[0]][index[1]] = value
        else:
            raise TypeError("Index must be an integer or a tuple of integers.")

    def __delitem__(self, index: Union[int, Tuple[int, int]]) -> None:
        if isinstance(index, int):
            del self._matrix[index]
            self.num_rows -= 1
        elif isinstance(index, tuple):
            del self._matrix[index[0]][index[1]]
            self.num_cols -= 1
        else:
            raise TypeError("Index must be an integer or a tuple of integers.")

    def __iter__(self) -> Iterable[Vector[T]]:
        return iter(self._matrix)

    def __contains__(self, other: Union[Vector[T], T]) -> bool:
        if isinstance(other, Vector):
            return any(other == vec for vec in self._matrix)
        elif isinstance(other, (int, float)):
            return any(other in vec for vec in self._matrix)
        else:
            return False

    def index(self, other: Union[Vector[T], T]) -> Tuple[int, int]:
        if isinstance(other, Vector):
            return self._matrix.index(other)
        elif isinstance(other, T):
            for i, vec in enumerate(self._matrix):
                if other in vec:
                    return i, vec.index(other)
            raise ValueError(f"{other} not found in matrix.")
        else:
            raise TypeError("Other must be a Vector or an element.")

    def __str__(self) -> str:
        return '\n'.join(str(vec) for vec in self._matrix)

    def __eq__(self, other: "Matrix[T]") -> bool:
        return self._matrix == other._matrix  # eq is implemented in Vector

    def clear(self) -> None:
        self._matrix = Vector()
        self.num_rows = 0
        self.num_cols = 0

    def reverse(self, order_by: int = 0) -> None:
        """
        Reverses the order of the rows or columns.
        
        Parameters:
            order_by: 0 for rows, 1 for columns.
        """
        if order_by == 0:
            self._matrix.reverse()
        elif order_by == 1:
            for vec in self._matrix:
                vec.reverse()
        else:
            raise ValueError("Order_by must be 0 (rows) or 1 (columns).")

    def transpose(self) -> "Matrix[T]":
        """
        Returns the transpose of the matrix.
        """
        return Matrix(elements=[[self._matrix[j][i] for j in range(self.num_rows)] for i in range(self.num_cols)])

    def minor(self, row: int, col: int) -> "Matrix[T]":
        """
        Returns the minor of the matrix.
        args:
            row: row index
            col: column index 
        """
        return Matrix(
            elements=[[self._matrix[i][j] for j in range(self.num_cols) if j != col] for i in range(self.num_rows) if
                      i != row])

    def determinant(self) -> T:
        """
        Returns the determinant of the matrix.
        """
        if self.num_rows != self.num_cols:
            raise ValueError("The matrix must be square.")
        if self.num_rows == 1:
            return self[0, 0]
        elif self.num_rows == 2:
            return self[0, 0] * self[1, 1] - self[0, 1] * self[1, 0]
        else:
            det = 0
            for j in range(self.num_cols):
                det += self[0, j] * self.cofactor(0, j)
            return det

    def cofactor(self, row: int, col: int) -> T:
        """
        Returns the cofactor of the matrix.
        """
        sign = (-1) ** (row + col)
        return sign * self.minor(row, col).determinant()

    def adjoint(self) -> "Matrix[T]":
        cofactors = [[self.cofactor(i, j) for j in range(self.num_cols)] for i in range(self.num_rows)]
        return Matrix(elements=cofactors).transpose()

    def inverse(self) -> "Matrix[T]":
        """
        Returns the inverse of the matrix.
        """
        det = self.determinant()
        if det == 0:
            raise ValueError("The matrix is singular (non-invertible).")
        if self.num_rows != self.num_cols:
            raise ValueError("The matrix must be square.")
        return self.adjoint() * (1 / det)

    def __add__(self, other: "Matrix[T]") -> "Matrix[T]":
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices must have the same dimensions.")
        return Matrix(elements=[[self._matrix[i][j] + other._matrix[i][j] for j in range(self.num_cols)] for i in
                                range(self.num_rows)])

    def __sub__(self, other: "Matrix[T]") -> "Matrix[T]":
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices must have the same dimensions.")
        return Matrix(elements=[[self._matrix[i][j] - other._matrix[i][j] for j in range(self.num_cols)] for i in
                                range(self.num_rows)])

    def __mul__(self, other: Union["Matrix[T]", T]) -> "Matrix[T]":
        if isinstance(other, Matrix):
            # Perform matrix multiplication if dimensions are valid.
            if self.num_cols != other.num_rows:
                raise ValueError(
                    "The number of columns of the first matrix must be equal to the number of rows of the second matrix."
                )
            new_elements = [
                [
                    sum(
                        self._matrix[i][k] * other._matrix[k][j]
                        for k in range(self.num_cols)
                    )
                    for j in range(other.num_cols)
                ]
                for i in range(self.num_rows)
            ]
            return Matrix(elements=new_elements)

        elif isinstance(other, (int, float)):
            # Perform scalar multiplication.
            new_elements = [
                [self._matrix[i][j] * other for j in range(self.num_cols)]
                for i in range(self.num_rows)
            ]
            return Matrix(elements=new_elements)

        else:
            raise TypeError("Other must be a Matrix or an element.")


class TestMatrix(unittest.TestCase):

    def test_init_elements_valid(self):
        # Initialize a 3x3 matrix.
        M = Matrix(elements=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(M.dims, (3, 3))
        self.assertEqual(M[0, 0], 1)
        self.assertEqual(M[2, 2], 9)

    def test_init_elements_invalid(self):
        # Inconsistent row lengths should trigger a ValueError.
        with self.assertRaises(ValueError):
            Matrix(elements=[[1, 2, 3], [4, 5]])

    def test_transpose(self):
        M = Matrix(elements=[[1, 2], [3, 4], [5, 6]])
        T = M.transpose()
        self.assertEqual(T.dims, (2, 3))
        self.assertEqual(T[0, 0], 1)
        self.assertEqual(T[1, 2], 6)

    def test_minor(self):
        # For a 3x3 matrix, the minor of position (0, 0)
        M = Matrix(elements=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        minor = M.minor(0, 0)
        # Expect the 2x2 matrix with elements [[5,6],[8,9]]
        self.assertEqual(minor.dims, (2, 2))
        self.assertEqual(minor[0, 0], 5)
        self.assertEqual(minor[1, 1], 9)

    def test_determinant_2x2(self):
        # determinant for [[1, 2], [3, 4]] is 1*4 - 2*3 = -2
        M = Matrix(elements=[[1, 2], [3, 4]])
        self.assertEqual(M.determinant(), -2)

    def test_determinant_3x3(self):
        # determinant for [[1,2,3],[0,1,4],[5,6,0]] is:
        # 1*(1*0-4*6) - 2*(0*0-4*5) + 3*(0*6-1*5) = -24 + 40 -15 = 1
        M = Matrix(elements=[[1, 2, 3], [0, 1, 4], [5, 6, 0]])
        self.assertEqual(M.determinant(), 1)

    def test_inverse(self):
        # Inverse of matrix:
        # [[4,7],[2,6]] is approximately [[0.6, -0.7], [-0.2, 0.4]]
        M = Matrix(elements=[[4, 7], [2, 6]])
        invM = M.inverse()
        self.assertAlmostEqual(invM[0, 0], 0.6, places=5)
        self.assertAlmostEqual(invM[0, 1], -0.7, places=5)
        self.assertAlmostEqual(invM[1, 0], -0.2, places=5)
        self.assertAlmostEqual(invM[1, 1], 0.4, places=5)

    def test_addition(self):
        M1 = Matrix(elements=[[1, 2], [3, 4]])
        M2 = Matrix(elements=[[5, 6], [7, 8]])
        M_add = M1 + M2
        self.assertEqual(M_add[0, 0], 6)
        self.assertEqual(M_add[1, 1], 12)

    def test_subtraction(self):
        M1 = Matrix(elements=[[5, 6], [7, 8]])
        M2 = Matrix(elements=[[1, 2], [3, 4]])
        M_sub = M1 - M2
        self.assertEqual(M_sub[0, 0], 4)
        self.assertEqual(M_sub[1, 1], 4)

    def test_matrix_multiplication(self):
        # Multiply [[1,2],[3,4]] * [[5,6],[7,8]] = [[19,22],[43,50]]
        M1 = Matrix(elements=[[1, 2], [3, 4]])
        M2 = Matrix(elements=[[5, 6], [7, 8]])
        M_mul = M1 * M2
        self.assertEqual(M_mul[0, 0], 19)
        self.assertEqual(M_mul[0, 1], 22)
        self.assertEqual(M_mul[1, 0], 43)
        self.assertEqual(M_mul[1, 1], 50)

    def test_scalar_multiplication(self):
        M = Matrix(elements=[[1, 2], [3, 4]])
        M_scaled = M * 3
        self.assertEqual(M_scaled[0, 0], 3)
        self.assertEqual(M_scaled[1, 1], 12)


if __name__ == '__main__':
    unittest.main()
