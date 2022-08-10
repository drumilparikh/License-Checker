import nltk
import pdb

def readlicense(name):

    with open(name, "r", encoding='utf-8-sig') as f:
        string = f.read()

    licenses=["MIT","Apache","Mozilla","GNU","BSD-3-Clause","BSD-2-Clause","Eclipse"]
    file_tokens=nltk.word_tokenize(string)
    s=set(licenses).intersection(file_tokens)
    m="".join(s)
    if("COMMON DEVELOPMENT AND DISTRIBUTED" in string.upper()):
        return "COMMON DEVELOPMENT AND DISTRIBUTED"
    elif(m=="GNU"):
            if("LESSER GENERAL PUBLIC" in string.upper()):
                return ("LGPL")
            else:
                return ("GPL")
    else:
        return m
    f.close()
