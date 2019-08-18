class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd=[]
        even=[]
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        temp=0
        ordered=[]
        i = 1
        j =1
        while(i < len(even)):
            if even[i] < even[i-1]:
                temp = even[i-1]
                even[i-1] = even[i]
                even[i]=temp
            i += 1
        while(j < len(odd)):
            if odd[j] < odd[j-1]:
                temp = odd[j-1]
                odd[j-1] = odd[j]
                odd[j]=temp
            j += 1
        print(odd, even)

        ordered=even+odd
        return ordered
