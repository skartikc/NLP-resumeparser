import json
import spacy
from tqdm import tqdm
from spacy.tokens import DocBin

with open('dataset/json/test/train_tra.json') as fp:
  TRAIN_DATA= json.load(fp)

nlp = spacy.blank('en')
db = DocBin()
for text, annot in tqdm(TRAIN_DATA['annotations']):
  doc = nlp.make_doc(text)
  ents = []
  for start, end, label in annot["entities"]:
    if label!='Email Address' and ((label!='Skills') or (label=='Skills' and (end-start)<18)):
      span = doc.char_span(start, end, label=label, alignment_mode="strict")
      if span is None:
        print("==Skipping Entity")
        print("start=" + str(start) + " " + str(end))
        print(text[start:end])
      elif span.text[0]==' ':
        # print(str(span.start_char) + " " + str(span.end_char))
        print('=WhiteSpace' + span.text)
      else:
        # print(str(span.start_char) + " " + str(span.end_char))
        ents.append(span)
        print("(" + span.text + ")" + span.label_)
    else:
      print("no mo 30 charactohs")
  doc.ents = ents
  db.add(doc)

db.to_disk("train_tra.spacy")
    

             