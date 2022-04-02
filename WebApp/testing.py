import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

from fuzzywuzzy import fuzz as fz
from fuzzywuzzy import process as pr
import csv
import re

import cv2
import numpy as np

import easyocr
from anonymize import OCR,fuzzy_matching,NLP,batchAnonymize


ocr = OCR()
# print(os.listdir('/Users/anishpawar/Downloads/static 2/outputs'))
batchAnonymize('/Users/anishpawar/Downloads/static 2/outputs/',ocr)

