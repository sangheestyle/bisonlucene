#!/usr/bin/env python

INDEX_DIR = "IndexFiles.index"
MAX_RESULT = 5

import sys, os, lucene
import collections

from java.io import File
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.util import Version
from org.apache.lucene.queries.mlt import MoreLikeThis

class SimilarToThis():

    def __init__(self):
        lucene.initVM(vmargs=['-Djava.awt.headless=true'])
        print 'lucene', lucene.VERSION

        self.base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.directory = SimpleFSDirectory(File(os.path.join(self.base_dir, INDEX_DIR)))
        self.reader = DirectoryReader.open(self.directory)
        self.searcher = IndexSearcher(self.reader)
        self.numDocs = self.reader.maxDoc()

        self.mlt = MoreLikeThis(self.reader)
        self.mlt.setMinTermFreq(1)
        self.mlt.setMinDocFreq(1)

        '''
        del searcher
        del reader
        del directory
        '''

    def getSimilarToThis(self, field="description", max=MAX_RESULT, path=INDEX_DIR):
        self.mlt.setFieldNames([field])

        for docID in range(self.numDocs):
            print "---"
            doc = self.reader.document(docID)
            print "title: " + doc.get('title')

            query = self.mlt.like(docID)

            similarDocs = self.searcher.search(query, max)
            if (similarDocs.totalHits == 0):
                print "None like this"

            for i in range(len(similarDocs.scoreDocs)):
                if similarDocs.scoreDocs[i].doc != docID:
                    doc = self.reader.document(similarDocs.scoreDocs[i].doc)
                    print "-> " \
                          + str(similarDocs.scoreDocs[i].score) \
                          + " : " \
                          + doc.getField('title').stringValue()

    def getTopNSimilarToThis(self, topN=0, field="description", max=MAX_RESULT, path=INDEX_DIR):
        if topN == 0:
            topN = self.numDocs

        self.mlt.setFieldNames([field])
        docList = {}

        for docID in range(self.numDocs):
            doc = self.reader.document(docID)
            query = self.mlt.like(docID)
            similarDocs = self.searcher.search(query, max)
            if (similarDocs.totalHits == 0):
                print "None like this"

            for i in range(len(similarDocs.scoreDocs)):
                if similarDocs.scoreDocs[i].doc != docID:
                    docList[similarDocs.scoreDocs[i].score] = [doc,
                                                               self.reader.document(similarDocs.scoreDocs[i].doc)]
        od = collections.OrderedDict(sorted(docList.items(), reverse=True))

        counter = 0
        for k, v in od.iteritems():
            counter += 1
            if counter > topN:
                break
            else:
                print "---"
                print k
                print v[0].getField('title').stringValue()
                print v[0].getField('playStoreURL').stringValue()
                print v[0].getField('creator').stringValue()
                print ".."
                print v[1].getField('title').stringValue()
                print v[1].getField('playStoreURL').stringValue()
                print v[1].getField('creator').stringValue()

if __name__ == '__main__':
    x = SimilarToThis()
    #x.getSimilarToThis()
    x.getTopNSimilarToThis(10)
