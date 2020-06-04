class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#recursive approach
#O(N) time, O(logN) space

def validateBst(tree):


	return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, min, max):


	if tree is None:
		return True

	if tree.value < min or tree.value >=max:
		return False

	return validateBstHelper(tree.left, min, tree.value) and validateBstHelper(tree.right, tree.value, max)
	
		

	
		


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

