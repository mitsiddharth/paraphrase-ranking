import io
import sys
import os

import analyze

WORD = sys.argv[1];

sorted_counts = analyze.getFeatureCounts('/scratch/cluster/sid/ukwac-matched-sentences/libsvm-files/' + sys.argv[1] + '.libsvm');

for i in range(10):
  print analyze.getWordFromFeatureID(sorted_counts[i][0], '/scratch/cluster/sid/ukwac-matched-sentences/unigrams/bright.unigrams'), sorted_counts[i][1]
