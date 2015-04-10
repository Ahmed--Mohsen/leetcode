class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        missing = 0
        for a in A:
            missing = missing ^ a
        return missing