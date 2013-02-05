import io
import sys

def getOriginalWords(line):
  token_array = line.split(' ');
  p = [];
  for token in token_array:
    wordDetails = token.split('|');
    p.append(wordDetails[0]);
  return p;
