# this is meant to extract the sentences out of the ukwac cnc-parsed files
# input should be those parts of the cnc-parsed files in which there are no
# comments, and no dependency information. All sentences starting with "<c>"
# should be given as input, after stripping out the "<c> " part.

import io
import sys

while True:
  try:
    line = raw_input();
    token_array = line.split(' ');
    p = [];
    for token in token_array:
      wordInfo = token.split('|');
      p.append(wordInfo[0]);
    print ' '.join(p);
  except EOFError:
    break;
