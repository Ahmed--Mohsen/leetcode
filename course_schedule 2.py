"""

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

"""
from collections import defaultdict

class Solution:
	# @param {integer} numCourses
	# @param {integer[][]} prerequisites
	# @return {integer[]}
	def findOrder(self, numCourses, prerequisites):
		
		# indegree[key] = value i.e. key = course label, value = in degree edge count
		in_degrees = [0] * numCourses
		
		# edge[key] = value i.e. key = source course, value = list of destination courses
		edge = defaultdict(list)
		
		# build in_degree counter
		for prerequisit in prerequisites:
			in_degrees[prerequisit[0]] += 1
			edge[prerequisit[1]].append(prerequisit[0])
			
		# get courses with zero dependency
		zero_dep = [i for (i, x) in enumerate(in_degrees) if x == 0 ]

		# check if no starting courses found
		if len(zero_dep) == 0:	return []
		
		courses = []
		finished = 0
		while zero_dep:
			current = zero_dep.pop()
			courses.append(current)
			finished += 1

			# decrease the dependencies of neighbour courses
			for course in edge[current]:
				in_degrees[course] -= 1
				if in_degrees[course] == 0: # to be finished
					zero_dep.append(course)
		
		# can finsihed if all courses have been taken
		if finished == numCourses:
			return courses
		else: #cycle exist
			return []
		
		


s = Solution()
print s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
			