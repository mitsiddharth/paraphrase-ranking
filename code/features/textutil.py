import io
import sys
import re

def process_text(text):
  text = re.sub("@\w+", ' ', text)
  text = re.sub("[0-9]",' ',text)
  text = re.sub("[\\:\[\]\"\(\);.,_+?\'/|#!$%^&*=-]",' ',text)
  while text.find('  ') != -1:
    text = text.replace('  ', ' ')
  return text.lower()

