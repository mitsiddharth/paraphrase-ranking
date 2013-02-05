# collect sentences from ukwac dataset that match any word from a set of
# paraphrases. writes the sentences grouped by that word.

import io
import sys
import os

import wordInfo

print >>sys.stderr, 'len(sys.argv) = ' + str(len(sys.argv));
print >>sys.stderr, 'sys.argv = ' + str(sys.argv);

NUM_WORDS = int(sys.argv[1]);
print >>sys.stderr, 'NUM_WORDS = ' + str(NUM_WORDS);

WORDS_TO_MATCH = sys.argv[2:2+NUM_WORDS];
print >>sys.stderr, 'WORDS_TO_MATCH = ' + str(WORDS_TO_MATCH);

OUTPUT_PATH = sys.argv[2+NUM_WORDS];
print >>sys.stderr, 'OUTPUT_PATH = ' + str(OUTPUT_PATH);

UKWAC_SEGMENT = sys.argv[2+NUM_WORDS+1];
print >>sys.stderr, 'UKWAC_SEGMENT = ' + str(UKWAC_SEGMENT);

fileDict = {};
for paraphrase in WORDS_TO_MATCH:
  fileDict[paraphrase] = open(OUTPUT_PATH + '/' + paraphrase + '/' + paraphrase + '.output', 'w');


while True:
  try:
    line = raw_input();
    words = wordInfo.getOriginalWords(line);
    unique_words = set(words);

    for word in unique_words:
      for paraphrase in WORDS_TO_MATCH:
        if word == paraphrase:
          print >>fileDict[word], ' '.join(words);
  except EOFError:
    break;

for file_ptr in fileDict:
  fileDict[file_ptr].close();
