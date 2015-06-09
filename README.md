# pdfAnalyse

A set of CLI tools:
  - parses the PDF to grab text
  - processes text generate a list of unique words
  - removes common words (taken from google's list of common US-English words)
  - generates a histogram 
  - turns histogram into a unique hash, easy for computing euclidian distances between papers

## Solves several problems:
Spits out the list of most common (scientifically relevant) words in a journal paper, helpful for identifying keywords when submitting a paper for publication.

A straight forward method for measuring how similar papers are. 

## Moving forward:
Next step is to add phrase analysis and look for common sets of words within a paper to identify important key phrases.

Long term goal run the hash generator over a set of papers from arXiv to identify similar papers and trends in research.
