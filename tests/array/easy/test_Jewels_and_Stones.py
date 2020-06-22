from solutions.array.easy.Jewel_and_Stones import Solution


def test():
    solution = Solution()
    assert solution.numJewelsInStones("aA", "aAAbbbb") == 3
