import io
import sys
from collections import defaultdict

def createFeatureMapping(featuresFile):
  id_count = 1;
  dic = defaultdict(int);
  f = open(featuresFile);
  lines = f.readlines();
  for line in lines:
    line = line.replace('\n', '');
    (ngram, count) = line.split('\t');
    if ngram not in dic:
      dic[ngram] = id_count;
      id_count += 1;
  f.close();
  return dic;

def save(featuresMapping, outputFile):
  f = open(outputFile, 'w');
  for key in featuresMapping:
    print >>f, str(key) + '\t' + str(featuresMapping[key]);
  f.close();

def load(filename, delimiter=' '):
  featuresMapping = defaultdict(int);
  f = open(filename);
  lines = f.readlines();
  for line in lines:
    line = line.replace('\n', '');
    (key, value) = line.split(delimiter);
    featuresMapping[key] = int(value);
  return featuresMapping;

# constructs and returns a dictionary that maps unigram's feature ID
# to the acutal unigram.
# eg. dic = { 1:'bright', 2135:'hello ...}
def loadIDToValue(filename, delimiter=' '):
  reverseMapping = defaultdict(int);
  f = open(filename);
  lines = f.readlines();
  for line in lines:
    line = line.replace('\n', '');
    (key, value) = line.split(delimiter);
    reverseMapping[int(value)] = key;
  return reverseMapping;

