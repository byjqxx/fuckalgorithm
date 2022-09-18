class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    # 在左子节点位置插入新节点
    # 如果左字节点为None：左子节点 = 新节点
    # 如果左子节点不为None：将新节点作为当前节点的子节点，当前节点的子节点降一级，成为新节点的左子节点
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    # 插入右子节点
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.rightChild
            self.rightChild = t

    # 访问二叉树
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key




r = BinaryTree('a')
print(r.getRootVal())
r.insertLeft('b')
r.insertRight('c')
print(r.getRightChild().getRootVal())
r.getLeftChild().setRootVal("hello")
print(r.getLeftChild().getRootVal())
