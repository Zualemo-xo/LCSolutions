# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)

        def traverse(node):
            if(node != None):
                print(node.val)
                d[node.val] += 1
                traverse(node.left)
                traverse(node.right)
        traverse(root)
        #print(d)
        #print(list(d.values()))
        ans = []
        count = max(list(d.values()))
        for i in d:
            if(d[i] == count):
                ans.append(i)
        #print(ans)
        return(ans)
        