from solutions.array.easy.Defanging_an_IP_Address import Solution


def test():
    solution = Solution()
    assert solution.defangIPaddr("1.2.3.4") == '1[.]2[.]3[.]4'
