import io
import sys
from collections import defaultdict

import textutil

def getDocument(text, featureMapping):
  documentVector = defaultdict(int);

  text = textutil.process_text(text);
  words = text.split(' ');
  for word in words:
    if len(word) == 0:
      continue;
    if word not in featureMapping:
      documentVector[len(featureMapping)] += 1;
    else:
      documentVector[featureMapping[word]] += 1;
  return documentVector;

def printDocument(documentVector, label):
  p = '';
  if len(label) > 0:
    p += str(label) + ' ';
  keys = documentVector.keys();
  keys.sort();
  for key in keys:
    p += str(key) + ':' + str(documentVector[key]) + ' ';
  print p;
