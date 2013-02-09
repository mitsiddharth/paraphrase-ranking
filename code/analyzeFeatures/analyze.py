import io
import sys
import os
import operator
from collections import defaultdict

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../features'))
if not path in sys.path:
  sys.path.insert(1, path);
del path

import featureMapping


# given a line from a libsvm file,
# this method returns a a tuple having 
# label as the first element, and dictionary
# containing feature ID as keys and
# feature values as values as 2nd element.
def getFeatureRow(line):
  arr = line.split(' ');
  # first element is label
  label = arr[0];
  dic = {};
  for i in range(1, len(arr)):
    if(len(arr[i])>1):
      (featureID, featureValue) = arr[i].split(':');
      dic[int(featureID)] = int(featureValue);
  return (label, dic);

# given a file path, finds the number of time each
# feature occurs in that file.
def getFeatureCounts(filename):
  f = open(filename);
  countsDict = defaultdict(int);
  line_cnt = 0;
  while True:
    try:
      line = f.readline();
      line_cnt += 1;
      if len(line) == 0:
        break;
      (label, dic) = getFeatureRow(line);
      for k in dic:
        countsDict[k] += 1;
    except EOFError:
      break;
  sorted_countsDict = sorted(countsDict.iteritems(), key = operator.itemgetter(1))
  sorted_countsDict.reverse();
  return sorted_countsDict;

def getWordFromFeatureID(featureID, featureFilePath):
  featuresDict = featureMapping.loadIDToValue(featureFilePath, '\t');
  if featureID in featuresDict:
    return featuresDict[featureID];
  else:
    return 'feature not found'
