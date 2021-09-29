

# Data Abstraction
# designing a link list 
# link example: [Head:6]->[5]->[9]->[4]->[3]->[Tail:2]
# a link list has a node known as head [1] that is linked to the next node
# element and tail that has no linked data


# The node object
class Node:
    """
        the node of each linked data element. 
        it is made to contain the data and a reference to the next_node data
    """
    def __init__(self, data):
        """
        initiate the data and the next node value
        
        arg: 
            data: the node data 
        """
        self.data = data
        self.next_node = None
    
    def __repr__(self):
        return "{}".format(self.data)
        
# the link iterator
class _LinkIterator:
    """the link iterator
        An iterator for linklist  
    """
    def __init__(self, the_head):
        
        self.current_node = the_head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_node  != None:
            item = self.current_node
            self.current_node  = self.current_node.next_node
            return item
        else:
            raise StopIteration
    
#the Link Object
class Link:
    """
        A link data abstraction: it is an improved python form of list that
        will help in improving the python list insertion and deletion complexity
        problem
     
    Behaviour(CRUD):
        prepend: add a new node to the head of the linklist
        Insert: insert any node at any given index
        search: check if a data is a member of the nodes in the linkedlist
        delete: delete any node any given index
        length: get the length of the list
    """
    head = None
    def __int__(self):
        """ Initiating the reference to the head node"""
        self.head = None
        
    def prepend(self, data):
        """
        append a node data at the beginging of the list
        
        time complexity -> O(1): constant time
        Arg: 
            data: the value of the new node to be added
        """
        previous_node = self.head
        new_node = Node(data)
        self.head = new_node
        new_node.next_node = previous_node 
        
    def postpend(self, data):
         """
         append a node at the end of the list
         
         Arg: 
            data: the value of the new node to be appended
            time complexity -> O(n): constant linear time
            
         """
         if self.head == None:
             return self.prepend(data) 
         
         else:
             new_node = Node(data)
             current_node = self.head
             
             while current_node.next_node:
                 current_node = current_node.next_node
                 
             current_node.next_node = new_node
         
    def __len__(linked_list):
        """
        the mothed that returns the number of  nodes on the list
        time complexity -> O(n): linear time
        
        Arg:
            lisked_list: the linked list
        
        return: the integer value of the total member of a linked list
        """
        # the starting node (i.e head)
        current_node = linked_list.head 
        length = 1
        
        # if there is no node on the linkedlist
        if current_node is None:
            return 0
        
        # while we have not reached the tail add 1 to length 
        while current_node.next_node:
            length += 1
            current_node =  current_node.next_node
        
        return length
    
    def length(self):
        """
        an alternative method that returns the length of the list
        
        time complexity -> O(n): linear time
        
        return: the integer value of the total member of a linked list
        """
        # the starting node (i.e head)
        return self.__len__(self)
    
    # the iterator
    def __iter__(self):
        return _LinkIterator(self.head)
    
    def insert(self, data, index):
        """
        Insert a data at any given position
        
        time complexity -> O(n): linear time
        Args:
            data: the data of the new node to be inserted
            index: the position of the new data to be inserted
            "-1" index insert at the end of the list while
            "1" index insert at the begining of the list 
        """
        n = len(self)
        if index >  n :
            raise IndexError("index:{} is greated than list length:{}".format(index, n))
        
        if index ==1:
            self.prepend(data)
            
        elif index == -1 or index == n:
            self.postpend(data)
        
        else:
            new_node = Node(data)
            position = index
            previous_node = None
            current_node = self.head
            next_node = current_node.next_node
            
            while position > 1 :
                position -=1
                previous_node = current_node
                current_node =next_node
                next_node = next_node.next_node
            
            previous_node.next_node = new_node
            new_node.next_node = current_node
    
    def search(self, data):
        
        """
        the search method that linearly check if an node data exist
         
         Arg: 
            data: the value of the node to be searched for
            time complexity -> O(n): constant linear time
            
        return: the node data or None
            
         """
        current_node = self.head
    
        if current_node == None :
            raise ValueError("Error: search is not possible on an empty list")
        while current_node: 
            if str(current_node) == str(data):
                return current_node
            current_node = current_node.next_node
        return None
        
    def index_of(self, data):
        
        """
        this returns the index of a node data on the list
         
         Arg: 
            data: the value of the node of which the index is needed
            time complexity -> O(n): constant linear time
        
        return: index(int) if found or -1
            
         """
        if self.search(data) == None:
            raise ValueError('data: {} does not exist'.format(data))
      
        index = 1
        for x in self:
            if str(x) == str(data):
                return index 
            index += 1
        return index
    
    def remove(self, data):
        
        """
        Remove a given node data
         
         Arg: 
            data: the value of the  node to be removed
            time complexity -> O(n): constant linear time
        
        return: the removed node
         """
        
        if self.search(data) == None:
            raise ValueError('data: {} does not exist'.format(data))
         
        if str(data) == str(self.head):
            self.head =self.head.next_node
            return self.head
        
        current_node = self.head
        previous_node = None
        found =False
        
        while current_node and found == False:
            if  str(data) == str(current_node):
                found = True
            else:
                previous_node = current_node
                current_node = current_node.next_node
            
        previous_node.next_node = current_node.next_node
        
        return current_node
    
    def __delitem__(self, index):
        
        """
        Remove a given node data
         
         Usage:
            del link_list[1]
            time complexity -> O(n): constant linear time
        
        return: the removed node
         """
        
        list_length  = len(self)
        
        if index ==1:
            self.head =self.head.next_node
            return self.head
        
        if index > list_length:
            raise IndexError("index: {} is out of range of list length".format(index))
                             
        elif list_length == 0:
            raise ValueError("linklist is empty")
        
        else:
        
           previous_node = self[index -1]
           current_node = self[index]
           
           previous_node.next_node = current_node.next_node
           
           return current_node
             
        
    def __getitem__(self, index):
        
        """
         get a node at a given index
         
         Arg: 
            index: position of the node to be obtained
            time complexity -> O(n): constant linear time
        
        return: the node
         """
         
        list_length  = len(self)
        
        if index > list_length:
            raise IndexError("index: {} is out of range of list length".format(index))
                             
        elif list_length == 0:
            raise ValueError("linklist is empty")
        
        else:
        
            node_element = None
            position = 1
            for node in self:
                if position == index:
                    node_element = node
                position +=1
                   
            return node_element
    
    def __setitem__(self, index, value):
        
        """
        set a given node at a given position to a given new data value
         
         Arg: 
            value:  the value of the  node to be set
            index: position of the node to be set
            
            time complexity -> O(n): constant linear time
        
        return: the removed node
         """
        
        if self.head is None:
            self.prepend(value)
        
        else:
           node = self[index]
           node.data = value
        
    def __repr__(self):
        
        nodes = []
        
        current_node = self.head
        
        while current_node:
            if current_node is self.head:
                nodes.append("[Head:%s]" % current_node.data)
            elif current_node.next_node is None:
                 nodes.append("[Tail:%s]" % current_node.data)
            else:
                nodes.append("[%s]" % current_node.data)
           
            current_node = current_node.next_node
            
        return "->".join(nodes)

    def sort(self, order="ASC"):
        the_list = self
        length = len(the_list)

        if length <=1:
            return the_list
    
        left, right, length = self._split(the_list, length)
        if length % 2 !=0:
            length += 1 
            
        left = self.sort(the_list)
        right = self.sort(the_list)

        return self._merge(left, right, order)

    def _split(self, the_list, length):
         
        mid = length//2
        left = Link()
        right = Link()
        position = 1
        rposition = mid + 1
        current_node = the_list.head 
        while position <=  mid:
            left.postpend(current_node)
            current_node = current_node.next_node
            position +=1
        
        while rposition <=  length:
            right.postpend(current_node)
            current_node = current_node.next_node
            rposition +=1

        if length > rposition:
            right.postpend(current_node.next_node)

        return left, right, mid

    def _merge(self, left, right, order):
        order = order
        l =  Link()
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                if order == "ASC":
                    l.postpend(left[i])
                    i +=1
                else:
                    l.prepend(left[i])
                    i +=1
            else:
                if order == "ASC":
                    l.postpend(right[j])
                    j +=1
                else:
                    l.prepend(right[j])
                    j +=1

        while i < len(left):
            if order == "ASC":
                l.postpend(left[i])
                i +=1
            else:
                l.prepend(left[i])
                i +=1
        while j < len(right):
            if order == "ASC":
                l.postpend(right[j])
                j +=1
            else:
                l.prepend(right[j])
                j +=1
        
        return l

    


"""
YOU CAN PLAY WITH THE LINK LIST CLASS BY PLAYING WITH IS METHODS LIKE:
    
    search
    prepend
    postpend
    index_of
    length
    remove
    
    and some defualt python list attributes like:
        the list being an iterable list (support for and while loop).
        the delete statement: del link[1]
        the assignment statement: link_list[1] = 5
        the get statement: link[1]
        the len(link_list)
    
"""
  
"""
FOR EXAMPLE RUN THE FOLLOWING LINES OF CODE
"""      
l = Link() # instatiate the link list

  
l.postpend(3)     
l.postpend(4)
l.postpend(2)
# l.insert(9, 1)

# l.insert(9, 1)
print(l.sort())


# for x in l:
#     print(x)
# print('-------')
# print(l.index_of(2))

# print(l)






