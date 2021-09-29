# from datetime import datetime\

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        


def tuple_2_tree(data):
    #print(data)
    if isinstance(data, tuple) and len(data)==3:
        node = Node(data[1])
        node.left = tuple_2_tree(data[0])
        node.right = tuple_2_tree(data[2])
    elif data is None:
        node = None
    else:
        node = Node(data)
    
    return node

data = ((4,7,12),2,((11, 5, None),8,9))
tree = tuple_2_tree(data)


def tree_2_tuple(tree):
    # stop the recursive function call when there is no sub node
    if tree is None:
        return None
    # stop the recursive node when you reach the leave node
    elif tree.left is None and tree.right is None:
        return tree.key
    else:
        root = tree.key
        left = tree_2_tuple(tree.left)
        right = tree_2_tuple(tree.right)

    return (left, root, right)

# print(tree_2_tuple(tree))

def inorder_tranverse(tree):
    if tree is None:
        return []
    elif tree.left is None and tree.right is None:
        return [tree.key]
    else:
        root = [tree.key]
        left = inorder_tranverse(tree.left)
        right = inorder_tranverse(tree.right)

    return left + root + right

# print(inorder_tranverse(tree)) 

def preorder_tranverse(tree):
    if tree is None:
        return []
    elif tree.left is None and tree.right is None:
        return [tree.key]
    else:
        root = [tree.key]
        left = preorder_tranverse(tree.left)
        right = preorder_tranverse(tree.right)

    return root + left + right

# print(preorder_tranverse(tree))

def postorder_tranverse(tree):
    if tree is None:
        return []
    elif tree.left is None and tree.right is None:
        return [tree.key]
    else:
        root = [tree.key]
        left = postorder_tranverse(tree.left)
        right = postorder_tranverse(tree.right)

    return  right + root + left
# print(postorder_tranverse(tree))  

def is_binary_serach_tree(tree):
    if tree is None:
        return True, None
    elif tree.left is None and tree.right is None:
        return True, tree.key
    else:
        root = tree.key
        is_bst_l, left = is_binary_serach_tree(tree.left)
        is_bst_r, right = is_binary_serach_tree(tree.right)

        is_bst = (is_bst_l and is_bst_r) and (left is None or left < root) and (right is None or right>root)
    return is_bst, root

# data_2 = (None,3,(None,5,None))
# bst_tree = tuple_2_tree(data_2)

# print(is_binary_serach_tree(bst_tree)[0])
def factorial(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return n  * factorial(n -1) 

# print(factorial(0))

def print_lines():
    print('-')
    print('--')
    print('-')
def draw_rule(n):
    if n>0:
        print('----'+ str(n))
        print_lines()
        n -= 1
        return draw_rule(n)
    
    

draw_rule(4)

def bst_min_max(tree):
    pass