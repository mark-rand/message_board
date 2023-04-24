from flaskr.canvas_array import CanvasArray


def test_append():
    ca = CanvasArray(height=2)
    ca.append([0, 0])
    assert ca.array == [[0, 0]]


def test_write():
    ca = CanvasArray(height=2)
    ca.write([0, 1], 0)
    assert ca.array == [[0, 1]]
    ca.write([2, 3], 0)
    assert ca.array == [[2, 3]]
    ca.append([-1, -1])
    assert ca.array == [[2, 3], [-1, -1]]
    ca.write([5, 6], 1)
    assert ca.array == [[2, 3], [5, 6]]
    """Ensure that alpha (-1) does not overwrite non-alpha"""
    ca.append([10, 11])
    assert ca.array[-1] == [10, 11]
    ca.write([-1, 12], len(ca.array) - 1)
    assert ca.array == [[2, 3], [5, 6], [10, 12]]


def test_add_background():
    ca = CanvasArray(height=2)
    ca.write([[-1, 1], [-1, 2]], 0)
    assert ca.array == [[-1, 1], [-1, 2]]
    assert ca.array_with_bg(3) == [[3, 1], [3, 2]]
    assert ca.array == [[-1, 1], [-1, 2]]
    ca.write([[-1, 3], [-1, 4]], len(ca.array))
    assert ca.array == [[-1, 1], [-1, 2], [-1, 3], [-1, 4]]
    assert ca.array_with_bg([9, 8, 7]) == [[9, 1], [8, 2], [7, 3], [9, 4]]
