"""Basic functionality of the project "Forward_list_vs_Bin_tree"."""
class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.count = 1
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def getCount(self):
        return self.count
    
    def setData(self, newdata):
        self.data = newdata
    
    def setNext(self, newnext):
        self.next = newnext
    
    def incCount(self):
        self.count += 1
    



# fwd_list Class
class FwdList(object):
    def __init__(self):
        self.head = None
    
    
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        
        while current != None and not stop:
            if current.getData() == item:
                current.incCount()
                stop = True
                return
                
            elif current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
                
        
        temp = Node(item)
        if previous == None:    # insert before first
            temp.setNext(self.head)
            self.head = temp
            
        else:
            temp.setNext(current)
            previous.setNext(temp)
    
    
    def print_list(self):
        current = self.head
        
        while current != None and current.getNext != None:
            print current.getData(), current.getCount()
            current = current.getNext()
        



# bin_tree Class
class TreeNode(object):
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        



class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0
    
    
    def length(self):
        return self.size


















