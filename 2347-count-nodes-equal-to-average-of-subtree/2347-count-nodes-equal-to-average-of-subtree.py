# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
count = 0
class Solution:
    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        global count
        count = 0
        def iterate(node):
            global count
            if(node != None):
                branch_sum_left, node_count_left = iterate(node.left)
                branch_sum_right, node_count_right = iterate(node.right)

                branch_sum = branch_sum_left + branch_sum_right + node.val
                node_count = node_count_left + node_count_right + 1
                if(int(branch_sum / node_count) == node.val):
                    count+=1
                return(branch_sum, node_count)

            else:
                return(0,0)
        
        iterate(root)
        return(count)


        