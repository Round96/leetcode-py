# Given a valid (IPv4) IP address, return a defanged version of that IP address.
#
#
#  A defanged IP address replaces every period "." with "[.]".
#
#
#  Example 1:
#  Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
#  Example 2:
#  Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"
#
#
#  Constraints:
#
#
#  The given address is a valid IPv4 address.
#  Related Topics String

# Runtime: 28 ms, faster than 73.85% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 13.9 MB, less than 27.41% of Python3 online submissions
# for Defanging an IP Address.
class Solution:
    def defangIPaddr(self, address: str) -> str:
        sub_address = address.split('.')
        return '[.]'.join(sub_address)

# Runtime: 20 ms, faster than 98.48% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 13.8 MB, less than 52.03% of Python3 online submissions for Defanging an IP Address.
# class Solution:
#    def defangIPaddr(self, address: str) -> str:
#        return address.replace('.', '[.]', 4)
