## SENTENCE CORRECTION

import numpy as np
import pandas as pd
import os
import re

######################################################################################
######################################################################################


curr_dir = os.path.dirname(__file__)

df_spell = pd.read_csv(os.path.join(curr_dir,'spell_corr.csv'),delimiter='|', header=None)
df_spell[0] = df_spell[0].apply(lambda x:x.lower())
df_spell[1] = df_spell[1].apply(lambda x:x.lower())
words = df_spell[0].tolist()
corrected_words = df_spell[1].tolist()

word_corr = {x:y for x,y in zip(words, corrected_words)}

######################################################################################
######################################################################################

def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i)<128)

def correct_(text):
    text = re.sub(r"'re"," are",text)
    text = re.sub(r"'s"," is",text)
    text = remove_non_ascii(text)
    
    text_ = text.split()
    
    for i in range(len(text_)):
        try:
            if str(text_[i].lower()) in word_corr:
                text_[i] = word_corr[str(text_[i].lower())]
        except:
            text_[i] = text_[i]


    res = " ".join(text_)
    if re.search(r"(\s)?\bam ",res) and not re.search(r"\b\s?(I|i) am ",res):
        res = re.sub(r"\b\s?am "," I am ",res)
    res = re.sub(r"\bi\b","I",res)
    text = re.sub("[\s]+"," ",text).strip()
    return res.strip()

