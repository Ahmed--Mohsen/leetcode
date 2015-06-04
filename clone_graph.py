# Definition for a undirected graph node
class UndirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []

def __hash__(self):
	return hash((self.label, str(self.neighbors)))

def __eq__(self, other):
	if other == None:
		return False
	return (self.label, self.neighbors) == (other.label, other.neighbors)

def __str__(self):
	neighborsLabels = ""
	for neighbor in self.neighbors:
		neighborsLabels = neighborsLabels + ", "+str(neighbor.label)
	return "label: "+str(self.label)+", neighbors: "+neighborsLabels
	
UndirectedGraphNode.__hash__ = __hash__
UndirectedGraphNode.__eq__ = __eq__
UndirectedGraphNode.__str__ = __str__

class Solution:
	# @param node, a undirected graph node
	# @return a undirected graph node
	def cloneGraph(self, node):
		if node == None:
			return None

		queue = [] #for BFS
		map = {} #key = real node label , value = copy node

		#copy head
		copyHead = UndirectedGraphNode(node.label)
		queue.append(node)
		map[node] = copyHead
		while(len(queue) != 0):
			current = queue.pop()
			copyCurrent = map[current]

			for neighbor in current.neighbors:
				if map.has_key(neighbor): #has been visited from another node
					copyCurrent.neighbors.append(map[neighbor])
				else: #new unvisited neighbor
					copyNeighbor = UndirectedGraphNode(neighbor.label)
					copyCurrent.neighbors.append(copyNeighbor)
					queue.append(neighbor) #to be seen
					map[neighbor] = copyNeighbor #mark as visited

		return copyHead
			
s = Solution()
u1 = UndirectedGraphNode(0)
u2 = UndirectedGraphNode(0)
u3 = UndirectedGraphNode(0)
u1.neighbors.append(u2)
u1.neighbors.append(u3)
s.cloneGraph(u1)