import spacy 
nlp = spacy.load("models\parser-try\model-best")
doc = nlp("ok baba. Ramnarain Ruia College, New Matunga. Pillai College of Engineering, New Panvel")
def countDep(doc,dep,tokid,end):
    count = 0
    for token in doc[tokid:end]:
        if str.lower(token.head.text) == "college" and token.dep_ == dep:
            count+=1
    return count
for token in doc:
    count = countDep(doc,"compound",1,9)
print("Counttttttttt = " + str(count))
