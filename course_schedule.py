"""

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.

"""

from collections import defaultdict

class Solution:
	
	# @param {integer} numCourses
	# @param {integer[][]} prerequisites
	# @return {boolean}
	def canFinish(self, numCourses, prerequisites):
		
		# indegree[key] = value i.e. key = course label, value = in degree edge count
		in_degrees = [0] * numCourses
		
		# edge[key] = value i.e. key = source course, value = list of destination courses
		edge = defaultdict(list)
		
		# build in_degree counter
		for prerequisit in prerequisites:
			in_degrees[prerequisit[0]] += 1
			edge[prerequisit[1]].append(prerequisit[0])
			
		# get courses with zero dependency
		zero_dep = []
		for i in range(len(in_degrees)):
			if in_degrees[i] == 0:
				zero_dep.append(i)

		# check if no starting courses found
		if len(zero_dep) == 0:
			return False
		
		finished = 0
		while zero_dep:
			current = zero_dep.pop()
			finished += 1

			# decrease the dependencies of neighbour courses
			for course in edge[current]:
				in_degrees[course] -= 1
				if in_degrees[course] == 0: # to be finished
					zero_dep.append(course)
		
		# can finsihed if all courses have been taken
		return finished == numCourses
		


s = Solution()
print s.canFinish(2, [])
			