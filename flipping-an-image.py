class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        #반전 후 역정렬
        #반전
        inv_img=[]
        for i in A:
            new_img=[]
            for j in i:
                if j == 1:
                    new_pix = 0
                elif j == 0:
                    new_pix = 1
                new_img.append(new_pix)
            inv_img.append(new_img)

        #역정렬
        flip_img=[]
        for i in range(len(inv_img)):
            rev_img=[]
            for j in range(1,len(inv_img[i])+1):
                rev_pix=inv_img[i][-j]
                rev_img.append(rev_pix)
            flip_img.append(rev_img)
        return flip_img
