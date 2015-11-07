"""

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

"""
class Solution:
	
	# @param version1, a string
	# @param version2, a string
	# @return an integer
	def compareVersion(self, version1, version2):
		if version1 == version2:
			return 0
		
		# parse the versions into integers
		v1 = [int(x) for x in version1.split(".")]
		v2 = [int(x) for x in version2.split(".")]
		
		# loop till both ends
		max_v = max(len(v1), len(v2))
		for i in range(max_v):
			a = v1[i] if i < len(v1) else 0
			b = v2[i] if i < len(v2) else 0
			
			# check if a and b are same or not
			compare = cmp(a, b)
			if compare != 0: return compare
		
		# passed all tests so must be equal
		return 0