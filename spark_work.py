import sys
from pyspark import SparkContext
import json

logfile = sys.argv[1]
sc = SparkContext()
logdata = sc.textFile(logfile).cache()
a_count = logdata.filter(lambda s: 'a' in s).count()
b_count = logdata.filter(lambda s: 'b' in s).count()
print(json.dumps({'a': a_count, 'b': b_count}))
