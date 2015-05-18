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
			