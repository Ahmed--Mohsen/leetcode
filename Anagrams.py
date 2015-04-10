import collections

class Solution:
	# @param strs, a list of strings
	# @return a list of strings
	def anagrams(self, strs):
		map = collections.defaultdict(list)
		for str in strs:
			str_key = tuple(sorted(str))
			map[str_key].append(str)
		
		result = []
		for anagram in map.values():
			if len(anagram) > 1:
				result += anagram
		return result

s = Solution()
print s.anagrams(["eat", "ate", "b"])