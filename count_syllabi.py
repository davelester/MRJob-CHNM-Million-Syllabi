from mrjob.job import MRJob

""" Counting the number of syllabi in the dataset """

class CountSyllabi(MRJob):
	""" For each line in the datset, a counter is yielded. """
	def mapper(self, _, line):
		yield 'syllabus_count', 1
	
	""" The reducer simply finds the sum of the data sent from the mapper, resulting in the number of syllabi """
	def reducer(self, key, values):
		yield(key, sum(values))
	
if __name__ == '__main__':
	CountSyllabi.run()