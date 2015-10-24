"""Basic functionality of the project "Forward_list_vs_Bin_tree"."""
glob_output = [] # global list for returning bin_tree nodes as list
glob_cmp_cnt = 0

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
        global glob_cmp_cnt 
        glob_cmp_cnt = 0
        self.head = None
        
        
    
    def add(self, item):
        global glob_cmp_cnt
        current = self.head
        previous = None
        stop = False
        
        while current != None and not stop:
            if current.getData() == item:
                glob_cmp_cnt += 1
                
                current.incCount()
                stop = True
                return
                
            elif current.getData() > item:
                glob_cmp_cnt += 2
                
                stop = True
            else:
                glob_cmp_cnt += 2
                
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
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.data = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        
    
    def has_left_child(self):
        return self.leftChild
    
    def has_right_child(self):
        return self.rightChild
    
    def is_left_child(self):
        return self.parent and self.parent.leftChild == self
    
    def is_right_child(self):
        return self.parent and self.parent.rightChild == self
    
    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return not (self.leftChild or self.rightChild)
    
    def has_any_children(self):
        return self.leftChild or self.rightChild
    
    def has_both_children(self):
        return self.leftChild and self.rightChild
    
    
    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.data = value
        self.leftChild = lc
        self.rightChild = rc
        
        if self.has_left_child():
            self.leftChild.parent = self
            
        if self.has_right_child():
            self.rightChild.parent = self
    
    
    def print_tree_node(self, offset):
        current = self
        
        if current.has_left_child():
            current.leftChild.print_tree_node(offset + 1)
                
        if current.has_right_child():
            current.rightChild.print_tree_node(offset + 1)
            
        print "." * offset, current.key, current.data
        
        



class BinarySearchTree(object):
    def __init__(self):
        global glob_cmp_cnt
        glob_cmp_cnt = 0
        self.root = None
        self.size = 0
    
    
    
    def put(self, key, val=1):
        if self.root:
            self._put(key, val, self.root)
        
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1
    
    
    def _put(self, key, val, currentNode):
        global glob_cmp_cnt
        
        if key == currentNode.key:
            glob_cmp_cnt += 1
            currentNode.data += 1
            
        elif key < currentNode.key:
            glob_cmp_cnt += 2
            if currentNode.has_left_child():
                self._put(key, val, currentNode.leftChild)
                
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            glob_cmp_cnt += 2
            if currentNode.has_right_child():
                self._put(key, val, currentNode.rightChild)
                
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
        
    
    
    def print_tree(self, offset=0):
        current = self.root
        
        if current != None:
            if current.has_left_child():
                current.leftChild.print_tree_node(offset + 1)
                
            if current.has_right_child():
                current.rightChild.print_tree_node(offset + 1)
            
            print "." * offset, current.key, current.data
        
    
    def get_all_nodes(self):
        
        if self.root:
            output = self._get_all_nodes(self.root)
        
        return output
    
    
    def _get_all_nodes(self, currentNode):
        global glob_output
        
        if currentNode.has_left_child():
            self._get_all_nodes(currentNode.leftChild)
            
        if currentNode.has_right_child():
            self._get_all_nodes(currentNode.rightChild)
        
        glob_output.append([currentNode.data, currentNode.key])
        return glob_output


















