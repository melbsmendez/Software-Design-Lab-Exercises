class SparseArray(object):

        def __init__(self,items=0):

            self.L = [0]*items

        def __setitem__(self, j, e):

            self.L[j] = e

        def __getitem__(self, j):

            return self.L[j]

        def __str__(self):

            return str(self.L)

sa=SparseArray(5)

sa[0]=(1,"a")

sa[1]=(2,"b")

sa[2]=(3,"c")

sa[3]=(4,"d")

sa[4]=(5,"e")

print("Sparse Array Content: \n",sa)