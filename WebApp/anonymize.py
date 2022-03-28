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

class OCR:
    def __init__(self) -> None:
        self.reader = easyocr.Reader(['en'])
    
    def detectText(self,image):
        self.image  = image
        self.ocrResult = self.reader.readtext(self.image)
        return self.ocrResult

    def drawBoundingBox(self):
        for i in self.ocrResult:
            self.bbImage = cv2.rectangle(self.image, i[0][0], i[0][2], (0,255,0), 5)
        return self.bbImage



def NLP(text):
    # global new_text
    # Text Pre-Processing
    text = text.split(' ')

    new = []

    for i in text:
        i = i.strip()
        
        a = i.replace('\n','')
        a2 = "".join(re.findall("[a-zA-Z]+", a))

        if len(i) > 2:
            new.append(a2.capitalize())

    # print(new)
    processed = " ".join(new)

    ne_tree = pos_tag(word_tokenize(processed))
    # print(ne_tree)
    names = []

    # Checking P-Noun Followed by P-Noun
    for c in range(len(ne_tree)):

        if ((ne_tree[c-1][1] == "NNP") and (ne_tree[c][1] == "NNP")) or ((ne_tree[c-1][1] == "NNP") and (ne_tree[c][1] == "NN")) or ((ne_tree[c-1][1] == "NN") and (ne_tree[c][1] == "NNP")):
            
            names.append(ne_tree[c-1][0])
            names.append(ne_tree[c][0])
    
    # If list is empty, return the original text
    if not names :
        for c in ne_tree:
            temp = "".join(re.findall("[a-zA-Z]+", c[0].lower()))
            # new_text.append(temp)
        return text
    
    
    else:
        # temp_list = names
        return set(names)

def fuzzy_matching(text):
    # global new_text
    # print(text)
    #Declarations
    new_text = []

    # if blur_stat == 0:

    Fname_ds = []
    Lname_ds = []
    body_part = ['abdomen', 'barium', 'bone', 'chest', 'dental', 'extremity', 'hand', 'joint', 'neck', 'pelvis', 'sinus', 'skull', 'spine', 'thoracic']

    print(text)

    #Opening CSV files
    with open('dependencies/Indian_Names.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for e in reader:
            # print(e)
            Fname_ds.append(e[1])

    with open('dependencies/indian_last_name.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)

        for e in reader:
            Lname_ds.append(e[0])


    if len(text) < 3 or pr.extractOne(text, body_part)[1] > 75: 
        return

    #Checking for first name
    for given in Fname_ds:
        if fz.ratio(text, given) > 60:
            # print(text, given, 1)
            new_text.append(text)
    
    #Checking for last name
    for given in Lname_ds:
        if fz.ratio(text, given) > 60:
            # print(text, given, 2)
            new_text.append(text)
    
    return new_text


def batchAnonymize(imgDir,ocr):
    # dstImg = f'{imgDir}/'
    print("IT")
    print(imgDir)
    # os.mkdir(f'{imgDir}/output')

    for imgSingle in os.listdir(imgDir):
        # print(f'{imgDir}/{i}')
        img = cv2.imread(f'{imgDir}/{imgSingle}')
        dat = ocr.detectText(img)
        
        textstr = ''
        for i in dat:
            textstr+= f'{i[1]} '
        
        textNLP = NLP(textstr)
        retlist = []
        for i in textNLP:
            retlist.append(fuzzy_matching(i))

        unique  = []
        for i in retlist:
            if i:
                unique.append(i[0])
        
        set(unique)
        dataDict = {'coords':[],'text':[]}

        for i in dat:
            # print(i)
            dataDict['coords'].append(i[0])
            dataDict['text'].append(i[1])
        
        coorList = []


        for i in set(unique):
            # print(i.lower())
            for j in range(len(dat)):
                text = dat[j][1].split(' ')
                for word in text:
                    if i.lower() == word.lower():
                        
                        coorList.append(dat[j][0])
        print("I Isss")
        print(imgSingle)
        for coor in coorList:
            img = cv2.rectangle(img, coor[0], coor[2], (0,255,0), -1)
        print("I Isss111")
        print(imgSingle)
        cv2.imwrite('static/output_img.jpg',img)
    return f'{imgDir[7:]}/x{imgSingle}'