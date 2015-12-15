# -*- coding: utf-8 -*-

"""

For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Hint:

How many MHTs can a graph have at most?
Note:

(1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”

(2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

"""

class Solution(object):
	
	"""
	:type n: int
	:type edges: List[List[int]]
	:rtype: List[int]
	"""
	def findMinHeightTrees(self, n, edges):
		# the idea is to move from the leave nodes and move
		# in-ward till we end up with either one or two roots
		# same idea as topological sort
		
		# base case
		if n == 1: return [0]
		
		# keep track of the the undirected edges
		adj = [set() for i in range(n)]
		for i, j in edges:
			adj[i].add(j)
			adj[j].add(i)

		# leaves are those nodes that have in-degree of length 1
		leaves = [i for i in range(n) if len(adj[i]) == 1]

		# do BFS topological sorting
		while n > 2:
			n -= len(leaves)
			
			# next level to the current leaves
			next_leaves = []
			
			# visit all neighbors to each leave
			for i in leaves:
				
				# no need to visit all i neighbors, we are only insterested
				# in the shortest path so any neighbor is valid
				j = adj[i].pop()
				adj[j].remove(i)
			
				# new leave found
				if len(adj[j]) == 1: 
					next_leaves.append(j)

			# set next level to be visited
			leaves = next_leaves
		
		return leaves
		
		
		
s = Solution()		
print s.findMinHeightTrees(4, [[1,0],[1,2],[1,3]])