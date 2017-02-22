def matrix(mat,mat1):
	result=0
	for x in range(len(mat)):
		for p in range(len(mat1[0])):
			for k in range(len(mat)):
				result[x][p]+=mat[x][k]*mat1[k][p]

	for t in result:
	    print (t)


import unittest

class TestStringMethods(unittest.TestCase):

    

    def test2(self):
       mat=[[1,1],[1,1]]
       mat1=[[1,1],[1,1]]
       self.assertTrue(matrix(len(mat[0])==len(mat1))

    

if __name__ == '__main__':
    unittest.main()