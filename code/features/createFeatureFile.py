import io
import sys
from collections import defaultdict

NUM_WORDS = int(sys.argv[1]);
WORDS = sys.argv[2:2+NUM_WORDS];
INPUT_PREFIX = sys.argv[2+NUM_WORDS];

unigrams = defaultdict(int);

for word in WORDS:
  f = open(INPUT_PREFIX + word);
  lines = f.readlines();
  for line in lines:
    line = line.replace('\n', '');
    (key, value_str) = line.split('\t');
    unigrams[key] += int(value_str);
  f.close();

unigram_cnt = 0;

for key in unigrams:
  unigram_cnt += 1;
  if unigrams[key] > 1:
    print str(key) + '\t' + str(unigram_cnt);
