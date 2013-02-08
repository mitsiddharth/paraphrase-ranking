import io
import sys
import paraphrases

TARGET_WORD = sys.argv[1];
GOLD_FILE = sys.argv[2];

paraphrases_list = paraphrases.getParaphrases(TARGET_WORD, GOLD_FILE);

print str(len(paraphrases_list)) + ' ' + ' '.join(paraphrases_list);
