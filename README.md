bisonlucene
===========
A simple prototype for indexing and searching based on PyLucene

##Object##

* Indexing files stored json format contents
* Searching term and phrase for description only (now)

##Requirement##

* Building and installing PyLucene 4.5 (for Mac): [Install Guide](https://medium.com/small-talk/e1e90a2b129f)

##Example##
###Indexing###
```
$ python IndexFiles [PathToFolderIncludingJsonFiles]
```

###Searching###
```
$ python SearchFiles,py
lucene 4.5.0

Hit enter with no input to quit.
Query:[InputHere]
```
Please refer [Apache Lucene Query parser syntax](http://lucene.apache.org/core/4_5_0/queryparser/org/apache/lucene/queryparser/classic/package-summary.html#package_description) to compose your own query set.

##Reference##

* This code is based on a sample provided by PyLucene project.
* Project information: http://goo.gl/ecSmCz
