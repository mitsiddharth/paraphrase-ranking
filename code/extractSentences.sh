#!/bin/bash

# input should be the .bz2 file containing
# (a segment) of ukwac data set.
# this script looks for sentences starting with "<c>"
# and outputs them by removing the "<c> " part. This output
# can be given to extractSentences.py to get the list of all
# original sentences in the ukwac dataset segment.

# this code is used in condor/extractSentences/ to get *all* sentences
# from the ukwac dataset.

bzcat $1 | grep "^<c>" | sed -n 's/^<c> \(.*\)/\1/p' | python /u/sid/paraphrase-ranking/code/extractSentences.py
