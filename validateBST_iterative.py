# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
	node = tree
	
	lst = [(node, float("-inf"), float("inf"))]
	
	while len(lst) > 0:
		
		print(lst,"---------")
		
		poped, min, max = lst.pop()
		
		if poped is None:
			continue
		
		if poped.value < min or poped.value >= max:
			return False
		
		lst.append((poped.left, min, poped.value))
		lst.append((poped.right, poped.value, max))
		print(lst,"########")
		
	return True
		

	
		


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)


print(validateBst(root))



# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

# import program
# import unittest


# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# class TestProgram(unittest.TestCase):
#     def test_case_1(self):
#         root = BST(10)
#         root.left = BST(5)
#         root.left.left = BST(2)
#         root.left.left.left = BST(1)
#         root.left.right = BST(5)
#         root.right = BST(15)
#         root.right.left = BST(13)
#         root.right.left.right = BST(14)
#         root.right.right = BST(22)
#         self.assertEqual(program.validateBst(root), True)
