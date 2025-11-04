def fun_type(fun):
    def wrapper(*args, **kwargs):
        print(type(fun))
        result = fun(*args, **kwargs)
        return result
    return wrapper

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


jc_tree_node1 = TreeNode(1)
jc_tree_node2 = TreeNode(2)
jc_tree_node3 = TreeNode(3)
jc_tree_node4 = TreeNode(4)
jc_tree_node5 = TreeNode(5)

jc_tree_node1.left = jc_tree_node2
jc_tree_node1.right = jc_tree_node3
jc_tree_node2.left = jc_tree_node4
jc_tree_node2.right = jc_tree_node5

#          1
#      2      3
#   4    5

#dfs preorder traversal without additional information passing
#preorder can be easily implemented with a stack
def dfs(node):
    if not node:
        return 
    print(f"pre-order dfs {node.val}")
    dfs(node.left)
    dfs(node.right)
    return 

dfs(jc_tree_node1)


# #dfs postorder traversal without additional information passing
# def dfs(node):
#     if not node:
#         return 
    
#     dfs(node.left)
#     dfs(node.right)
#     print(f"post-order dfs {node.val}")
#     return 

# dfs(jc_tree_node1)