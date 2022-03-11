import pandas as pd

df = pd.read_csv ('dataset/gsheet.csv', usecols=['text'])

def remove_emojis(text):
    spl = """"#$%&'()*+, -./<=>?@[\]^_{|}~"""
    Ualp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Lalp = "abcdefghijklmnopqrstuvwxyz"
    dig = "0123456789"
    extras = " "
    no_punct=[words for words in text if (words in spl) or (words in dig) or (words in Ualp) or (words in Lalp) or (words in extras)]
    words_wo_punct=''.join(no_punct)
    return words_wo_punct


def remove_white(text):
    i=0
    for _ in text:
        if i==(len(text)-1):
            break
        if text[i] == " ":
            for j in range(1,6):
                if text[i+j]!=" ":
                    break
            if j!=1:
                wstr = j*" "
                text = text.replace(wstr," ")
        i=i+1        
    return text

for i in range(0,len(df)):
    text = df['text'][i]
    text = text.replace("\n","$").replace("&nbsp;","")
    with open(f"dataset/text/individual/resume{i}.txt",'w', encoding="utf-8") as f:
        f.write(text)

textF = "" 

for i in range(0,len(df)):
    with open(f"dataset/text/individual/resume{i}.txt","r",encoding="utf-8") as f:
        text1 = f.read()
    text1 = text1.replace("\n"," ").replace("$"," ").replace("\\n",' ')
    text1 = remove_white(text1)
    text1 = remove_emojis(text1)
    with open(f"dataset/text/individual/resume{i}.txt","w",encoding="utf-8") as f:
        f.write(text1)
    textF = textF + text1 + "\n"

with open(f"dataset/text/annotator.txt","w",encoding="utf-8") as f:
    f.write(textF)
    
    
