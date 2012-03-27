#MapReduce Jobs for CHNM's Million Syllabi Database

**Description:**

This repository contains a series of MapReduce jobs that run on a sample of ~~50,000 syllabi~~ 100 syllabi from [CHNM's million syllabi database](http://www.dancohen.org/2011/03/30/a-million-syllabi/). They can also be used on the entire million+ dataset, however only a subset of the data has been cleaned and reformatted at this time. MapReduce jobs are written in Python, using [MRJob](https://github.com/Yelp/mrjob).


**Contents:**

* /data/ - Includes syllabi_sample.txt, which is the first 100 records from the CHNM syllabi database.
* average_words_per_syllabus.py - Calculate the average number of words per syllabus text.
* count_syllabi.py - Count the number of syllabi in the dataset. This is the most-basic example of map reduce and using MRJob I could write.
* count_unique_domains.py - 
* syllabus_similarity_jaccard_index.py - 


**Contribute:**

There are 