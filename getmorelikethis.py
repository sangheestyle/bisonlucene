#!/usr/bin/env python

INDEX_DIR = "IndexFiles.index"
MAX_RESULT = 5

import sys, os, lucene

from java.io import File
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.util import Version
from org.apache.lucene.queries.mlt import MoreLikeThis


if __name__ == '__main__':
    lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    print 'lucene', lucene.VERSION
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    directory = SimpleFSDirectory(File(os.path.join(base_dir, INDEX_DIR)))
    reader = DirectoryReader.open(directory)
    searcher = IndexSearcher(reader)
    numDocs = reader.maxDoc()

    mlt = MoreLikeThis(reader)
    mlt.setFieldNames(['description'])
    mlt.setMinTermFreq(1)
    mlt.setMinDocFreq(1)

    for docID in range(numDocs):
        print "---"
        doc = reader.document(docID)
        print "title: " + doc.get('title')

        query = mlt.like(docID)

        similarDocs = searcher.search(query, MAX_RESULT)
        if (similarDocs.totalHits == 0):
            print "None like this"

        for i in range(len(similarDocs.scoreDocs)):
            if similarDocs.scoreDocs[i].doc != docID:
                doc = reader.document(similarDocs.scoreDocs[i].doc)
                print "-> " \
                      + str(similarDocs.scoreDocs[i].score) \
                      + " : " \
                      + doc.getField('title').stringValue()

    del searcher
    del reader
    del directory
