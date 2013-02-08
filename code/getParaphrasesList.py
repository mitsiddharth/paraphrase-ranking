import io
import sys
import paraphrases

NUM_TARGET_WORDS = int(sys.argv[1]);
TARGET_WORDS = sys.argv[2:2+NUM_TARGET_WORDS];
GOLD_FILE = sys.argv[2 + NUM_TARGET_WORDS];

paraphrases_list = [];

for target_word in TARGET_WORDS:
  l = paraphrases.getParaphrases(target_word, GOLD_FILE);
  for w in l:
    paraphrases_list.append(w);

paraphrases_list = list(set(paraphrases_list));

print str(len(paraphrases_list)) + ' ' + ' '.join(paraphrases_list);
