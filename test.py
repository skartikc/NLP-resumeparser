import spacy 
nlp = spacy.load("en_pipeline")
doc = nlp("ok baba. Ramnarain Ruia College, New Matunga. Pillai College of Engineering, New Panvel")

print(nlp._path)
for ent in doc.ents:
    print(ent.label_,ent.text)
