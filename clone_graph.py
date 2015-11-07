"""

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

"""

# Definition for a undirected graph node
class UndirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []
	

class Solution:
	
	# @param node, a undirected graph node
	# @return a undirected graph node
	def cloneGraph(self, node):
		if node == None:
			return None

		queue = [] # for BFS
		map = {} # key = real node label , value = copy node

		#copy head
		copyHead = self.getNodeCopy(map, queue, node)
		
		while queue:

			# copy current node
			current = queue.pop()
			copyCurrent = self.getNodeCopy(map, queue, current)
			
			# copy its neighbors
			for neighbor in current.neighbors:
				# copy neighbor
				copyNeighbor = self.getNodeCopy(map, queue, neighbor)
				
				# set undirected edge
				copyCurrent.neighbors.append(copyNeighbor)

		return copyHead
		
	"""
	get a copy node for the input node
	if the node copy already existed before its just returned
	"""
	def getNodeCopy(self, map, queue,  node):
		# not copied before
		if not node.label in map:
			copy = UndirectedGraphNode(node.label)
			map[node.label] = copy
			queue.append(node)
			
		return map[node.label]
		
			
s = Solution()
u1 = UndirectedGraphNode(0)
u1.neighbors.append(u1)
s.cloneGraph(u1)