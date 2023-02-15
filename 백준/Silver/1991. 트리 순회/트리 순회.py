import sys

input = sys.stdin.readline
N = int(input().strip())

class Node():
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

def preorder(node):
    print(node.root, end = '')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.root, end='')
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.root, end='')

arr = []
tree = {}
for _ in range(N):
    arr.append(input().split())
for root, left, right in arr:
    tree[root] = Node(root, left, right)
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])