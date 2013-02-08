import io
import sys
import featureMapping
import document
from collections import defaultdict

TEXT_FILE = sys.argv[1];
print >>sys.stderr, 'TEXT_FILE = ' + str(TEXT_FILE);

LABEL = sys.argv[2];
print >>sys.stderr, 'LABEL = ' + str(LABEL);

FEATURES_FILE = sys.argv[3];
print >>sys.stderr, 'FEATURES_FILE = ' + str(FEATURES_FILE);

featuresDict = featureMapping.createFeatureMapping(FEATURES_FILE);
f = open(TEXT_FILE);
tweets = f.readlines();
for tweet in tweets:
  tweet = tweet.replace('\n', '');
  documentVector = document.getDocument(tweet, featuresDict);
  document.printDocument(documentVector, str(LABEL));
