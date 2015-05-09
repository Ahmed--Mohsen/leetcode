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
			