#!/usr/bin/python

import sys
import re
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFPageInterpreter

from boringWords import boringWords
#Turns a pdf into a string, totally naive might not correctly implement new lines.
def pdf2str(path):

    #Allocate resources
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    
    #Set parameters
    codec = 'utf-8'
    laparams.all_texts=True
    laparams.detect_vertical = True
    caching = True
    pagenos = set()

    #Initialize the converter
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)

    #Open the file and parse
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in PDFPage.get_pages(fp, pagenos,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    #Clean up
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

#Generates a count of relevant words from a single string
#Attempts to remove punctuation and ugly characters
def wordCount(fullText):

    #Get Rid of punctuation and newlines
    for ch2null in [",",":",";","-\n"]:
        fullText = fullText.replace(ch2null,"")
    
    #Insert spaces over some punctuation
    for ch2space in ["(",")",". "]:
        fullText = fullText.replace(ch2space," ")

    #Replace unicode that gets missed by the converter.
    fullText = fullText.replace("\xe2\x80\x93","-") 
    fullText = fullText.replace("\xef\xac\x80","ff") 
    fullText = fullText.replace("\xef\xac\x82","fl")

    #Get those uniques
    words = fullText.lower().split()
    uniques = list(set(words)-boringWords)

    #Remove single letter uniques
    uniques = [u for u in uniques if len(u)>1]

    #Remove numbers (floats/ints) from the uniques
    uniques = [u for u in uniques if re.match("^\d+?\.?\d+?$", u)==None ]

    #Figure out a way to remove Reference data from histogram, not easy...

    #Start Counting words
    counts = [words.count(u) for u in uniques]
    wordCounts = sorted(zip(counts,uniques),key=lambda x:x[0])
    
    return wordCounts

#Takes in a histogram that is count-word pairs and turns it into a hash
def count2hash(wordCounts):
    pass

#Reverse of count2hash function, turns a hash into a list of count-word pairs
def hash2count(hashed):
    pass

#Returns the euclidian distance between 2 hashes.
def euclidDistance(hash1,hash2):
    pass

if __name__=="__main__":
    
    fullText = pdf2str(sys.argv[1])
    wordCounts = wordCount(fullText)

    for w in wordCounts:
        print w
