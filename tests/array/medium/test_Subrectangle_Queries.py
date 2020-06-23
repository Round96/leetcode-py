from solutions.array.medium.Subrectangle_Queries import SubrectangleQueries


def test():
    subrectangleQueries = SubrectangleQueries(
        [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])

    assert subrectangleQueries.getValue(0, 2) == 1

    subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5)

    assert subrectangleQueries.getValue(0, 2) == 5
    assert subrectangleQueries.getValue(3, 1) == 5

    subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10)

    assert subrectangleQueries.getValue(3, 1) == 10
    assert subrectangleQueries.getValue(0, 2) == 5
