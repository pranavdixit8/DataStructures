
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if self is None:
            self = BST(value)

        if self.value > value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
        
        return self

    def contains(self, value):

        if self.value == value:
            return True

        if self.value > value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

        return False
        


    def remove(self, value, parent = None):

        if self.value == value:

            if self.left and self.right:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)

            elif parent is None:
                if self.left:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                if self.right:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
            elif parent.left == self:
                parent.left = self.left if self.left else self.right
            elif parent.right == self:
                parent.right = self.left if self.left else self.right

        if self.value > value:
            if self.left is None:
                return self
            else:
                return self.left.remove(value, self)
        else:
            if self.right is None:
                return self
            else:
                return self.right.remove(value,self)


        



        return self


    def getMinValue(self):

        currentNode = self

        while currentNode.left:
            currentNode = currentNode.left

        return currentNode.value















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

print(root.contains(3))