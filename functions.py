import pandas 
import string
import matplotlib.pyplot
import re


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import PorterStemmer

from pymystem3 import Mystem



def create_ann(annatation: str) -> pandas.DataFrame:

    """Создаёт датафрейм по пути аннатации"""

    frame = pandas.DataFrame(columns =["Оценка","Kоличество слов","Текст рецензии"])
    ann_temp = open(annatation, "r", encoding="utf-8")
    for otzv in ann_temp.readlines():
        mas_otzv = otzv.split(",")
        otzv_temp = open(mas_otzv[0],"r",encoding="utf-8")
        otzv_text = " ".join(otzv_temp)
        row = pandas.Series({"Оценка": int(mas_otzv[2]),"Kоличество слов": len(otzv_text), "Текст рецензии": otzv_text})
        new_row = pandas.DataFrame([row], columns=frame.columns)
        frame = pandas.concat([frame, new_row], ignore_index=True)
    frame.dropna()
    return frame

def clean (frame: pandas.DataFrame) -> pandas.DataFrame:
    remove_non_alphabets =lambda x: re.sub(r'[^а-яА-Я]','',x)
    print('Processing : [=')
    frame["Текст рецензии"] = frame["Текст рецензии"].apply(remove_non_alphabets)
    print('=')
    frame["Текст рецензии"] = frame["Текст рецензии"].apply(Mystem().lemmatize)
    print('=')
    frame["Текст рецензии"] = frame["Текст рецензии"].apply(lambda x: ' '.join(x))
    print('] : Completed')
    return frame


