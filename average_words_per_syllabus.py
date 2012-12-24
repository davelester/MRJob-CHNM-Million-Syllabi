from mrjob.job import MRJob
import re
 
WORD_RE = re.compile(r"[\w']+")

""" What is the average number of words per syllabus? """

class AverageWordsPerSyllabus(MRJob):
 
	""" retrieves a syllabus, and returns its length """
	def get_syllabus_text_len(self, _, line):
		syllabus = line.split('\t')
		word_count = len(WORD_RE.findall(syllabus[6]))
		yield 'word_count', word_count
		yield 'syllabus_count', 1

	""" add together the counts """
	def add_counts(self, key, value):
		yield key, sum(value)

	""" join counts together, assigning to a key called total """
	def join_syllabus_words_count_and_review_count(self, key, counter):
		yield 'total', (key, counter)

	""" divide the count of total words by number of total syllabi, and yield the average """
	def average_syllabus_word_count(self, key, counter):
		syllabus_count = 0
		word_count = 0
		for tuple in counter:
			if tuple[0] == 'word_count':
				word_count = tuple[1]
			if tuple[0] == 'syllabus_count':
				syllabus_count = tuple[1]
		yield 'average', float(word_count) / syllabus_count

	def steps(self):
		return [self.mr(mapper=self.get_syllabus_text_len, reducer=self.add_counts),
				self.mr(mapper=self.join_syllabus_words_count_and_review_count, reducer=self.average_syllabus_word_count)] 
 
if __name__ == '__main__':
	AverageWordsPerSyllabus.run()
