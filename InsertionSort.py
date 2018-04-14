import utilities

class InsertionSort():

	# Sort an array using Selection Sort
	def sort_array(self, array):
		
		# Loop through the entire array
		for current_foward in range( 1, len(array) ):
			
			# Go on each element before the current

			current_backwards = current_foward
			# Check which word comes first in alphabetic order

			this = array[current_backwards-1]
			that = array[current_backwards]

			# Do it whithout going out of the array boundery
			while current_backwards > 0 and utilities.this_word_comes_first_than_that(this,that):
					
					# Swap the words

					i = current_backwards
					j = (current_backwards - 1)

					array[i],array[j] = array[j],array[i]

					# Update their indexes to go even futher in the array
					current_backwards -= 1

					this = array[current_backwards-1]
					that = array[current_backwards]

			

