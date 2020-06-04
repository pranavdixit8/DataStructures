#iterative appraoch



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

    	currentNode = self

    	if currentNode is None:
    		self = BST(value)

    	while currentNode:

    		if currentNode.value > value:
    			if currentNode.left is None:
    				currentNode.left = BST(value)
    				break
    			else:
    				currentNode = currentNode.left
    		else:
    			if currentNode.right is None:
    				currentNode.right = BST(value)
    				break
    			else:
    				currentNode = currentNode.right
        
		
        return self

    def contains(self, value):

    	currentNode = self

    	while currentNode:

    		if currentNode.value > value:
    			currentNode = currentNode.left
    		elif currentNode.value < value:
    			currentNode = currentNode.right
    		else:
    			return True

    	return False
       

    def remove(self, value, parentNode = None):

    	# search for the node

    	currentNode = self

    	while currentNode:

    		if currentNode.value > value:
    			parentNode = currentNode
    			currentNode = currentNode.left
    		elif currentNode.value < value:
    			parentNode = currentNode
    			currentNode = currentNode.right
    		else:

    			#once found hendle all the cases

    			if currentNode.left and currentNode.right:
    				currentNode.value = currentNode.right.getMinValue()
    				currentNode.right.remove(currentNode.value, currentNode)

    			elif parentNode is None:

    				if currentNode.left:
    					currentNode.value = currentNode.left.value
    					currentNode.right = currentNode.left.right
    					currentNode.left = currentNode.left.left
    				
    				elif currentNode.right:
    					currentNode.value = currentNode.right.value
    					currentNode.left = currentNode.right.left
    					currentNode.right = currentNode.right.right
    				else:
    					break

    			elif parentNode.left == currentNode:
    				parentNode.left = currentNode.left if currentNode.left else currentNode.right

    			elif parentNode.right == currentNode:
    				parentNode.right = currentNode.left if currentNode.left else currentNode.right

    			break

       
        return self

    def getMinValue(self):
		node = self
		while node.left:
			node = node.left
		
		return node.value


#test


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

root.insert(12)

print(root.right.left.left.value == 12)

root.remove(10)

print(not root.contains(10))

print(root.value == 12)

print(root.contains(15))
