class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#iterative approach (BFS)
#O(N) time, O(logN) space

def validateBst(tree):
	node = tree
	
	lst = [(node, float("-inf"), float("inf"))]
	
	while len(lst) > 0:
		
		poped, min, max = lst.pop(0)

		
		if poped is None:
			continue
		# else:
		# 	print(poped.value)
		
		if poped.value < min or poped.value >= max:
			return False
		
		lst.append((poped.left, min, poped.value))
		lst.append((poped.right, poped.value, max))
		
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

