import nltk
import pdb

def readlicense(name):

    with open(name, "r", encoding='utf-8-sig') as f:
        string = f.read()

    licenses=["MIT","Apache","Mozilla","GNU general public","gnu public general public", "gnu affero general public LICENSE","BSD-3-Clause"]
    file_tokens=nltk.word_tokenize(string)
    # print(file_tokens)
    # for x in file_tokens:
    #     for string1 in licenses:
    #        if (string1.upper() == x.upper()):
    #             # pdb.set_trace()
    #             return(string1.upper())
    #             break
    #             break

    s=set(licenses).intersection(file_tokens)
    m="".join(s)
    return m
    f.close()
# if(readlicense("/home/drumil/Downloads/travelwebsite/like_button.js")):
#     print("Hello")
