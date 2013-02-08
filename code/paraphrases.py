import io
import sys

def getRHSwords(line):
  ret = set();
  pos = line.rfind(':');
  paraphraseInfo_array = line[pos+1:].split(';');
  for entry in paraphraseInfo_array:
    entry = entry.strip();
    # found hyphenated word -- so, ignore.
    if(entry.find('-') != -1):
      continue;
    arr = entry.split(' ');
    # this should happen only for multi-word paraphrases.
    # ignore such paraphrases
    if len(arr) > 2:
      continue;
    if len(arr[0]) > 0:
      ret.add(arr[0]);
  return ret;


def getParaphrases(target_word, gold_file_name):
  ret = set();
  f = open(gold_file_name);
  lines = f.readlines();
  for line in lines:
    line = line.replace('\n', '');
    # the line in gold file starts with the target word that we are looking for
    if line.find(target_word + '.') == 0:
      l = getRHSwords(line);
      for p in l:
        ret.add(p);
  return list(ret);
