"""

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.

"""

class Solution:
  # @param {integer} A
  # @param {integer} B
  # @param {integer} C
  # @param {integer} D
  # @param {integer} E
  # @param {integer} F
  # @param {integer} G
  # @param {integer} H
  # @return {integer}
  def computeArea(self, A, B, C, D, E, F, G, H):
		# calc each area seperately
		area_1 = (C-A) * (D-B)
		area_2 = (G-E) * (H-F)
		
		# calc boundries
		left = max(A, E)
		right = min(G, C)
		top = min(D, H)
		bottom = max(B, F)
		
		# check if intersection occur
		intersection = 0
		if right > left and top > bottom:
			intersection = (right - left) * (top - bottom)
		
		return area_1 + area_2 - intersection
