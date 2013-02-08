import io
import sys
from collections import defaultdict

def magnitude(vector):
  magnitude = 0.0;
  for i in vector:
    magnitude += vector[i]**2;
  magnitude = magnitude ** 0.5;
  return magnitude;

def normalize(vector):
  mag = magnitude(vector);
  for i in vector:
    vector[i] /= mag;
  return vector;

def getDocument(tweetText, featureMapping):
  documentVector = defaultdict(int);
  for n in range(1, 6):
    for i in range(0, len(tweetText)-(n-1)):
      ngram = tweetText[i:i+n]
      if ngram not in featureMapping:
        documentVector[len(featureMapping)] += 1;
      else:
        documentVector[featureMapping[ngram]] += 1;
  #documentVector = normalize(documentVector);
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
