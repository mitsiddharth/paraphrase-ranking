import io
import sys
import os
from collections import defaultdict

NUM_WORDS = int(sys.argv[1]);
WORDS = sys.argv[2:2+NUM_WORDS];
SENTENCES_PATH=sys.argv[2+NUM_WORDS];
PREFIX = sys.argv[3+NUM_WORDS];

for word in WORDS:
  cmd = "ls -1 " + SENTENCES_PATH + "/*/" + word + "/" + word + ".output | xargs cat | /u/sid/paraphrase-ranking/ngrams/ngrams --n=1 --type=word > " + PREFIX + word;
  print >>sys.stderr, "cmd = " + cmd;
  os.system(cmd);

unigrams = defaultdict(int);

for word in WORDS:
  f = open(PREFIX + word);
  lines = f.readlines();
  for line in lines:
    line = line.replace('\n', '');
    (key, value_str) = line.split('\t');
    unigrams[key] += int(value_str);
  f.close();

unigram_cnt = 0;

for key in unigrams:
  if unigrams[key] > 10:
    unigram_cnt += 1;
    print str(key) + '\t' + str(unigram_cnt);
