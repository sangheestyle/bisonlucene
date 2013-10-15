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

###Searching examples###
A single term searches
```
title:"camera"
description:"camera"
description:camera
```

A parse searches
```
description:"camera location"
description:"location camera"
```

Fields searches: Lucene supports fielded data.
```
description:"camera location" AND title:"CA"
```

Boolean operators searches
```
description:"camera" AND description:"location"
description:"camera" OR description:"location"
```

Proximity Searches: Lucene supports finding words are a within a specific distance away. To do a proximity search use the tilde, "~" (e.g. ~5 means within 5 words)
```
description:"camera location"~5
```

Regular Expression Searches: Lucene supports regular expression searches matching a pattern between forward slashes "/"
```
description:/[mb]oat/
```

##Reference##

* This code is based on a sample provided by PyLucene project.
* Project information: http://goo.gl/ecSmCz
