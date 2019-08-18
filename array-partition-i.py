class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        absA=[]
        for i in A:
            absA.append(abs(i))
        sqrA=[]
        for i in absA:
            sqr = i**2
            sqrA.append(sqr)


        for i in range(len(sqrA)):
            j=1
            while(j<len(sqrA)):
                if sqrA[j-1] > sqrA[i]:
                    sqrA[j-1], sqrA[i] = sqrA[i], sqrA[j-1]
                else:
                    j += 1
        return sqrA
