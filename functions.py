from ctypes import alignment
import spacy
from spacy.language import Language
from spacy.matcher import DependencyMatcher
import re
nlp = spacy.load('en_core_web_lg')
@Language.component("email_phone_ner")
def email_phone_ner_fact(doc):
    reForEmail = r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
    reForEmail2 = r"indeed.com/r/[a-zA-Z-0-9]+/[a-zA-Z0-9-]+"
    reForNumba = r"((?=\+\d{3}\s?)\+\d{3}\s?\d{4}\s?\d{4,5}|(\+\d{0,2}\s?)?((?=1)(1?\-?\.?\s?)|)\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})"
    ents = []
    for match in re.finditer(reForNumba, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end, label="PHONE")
        if span is not None:
            ents.append(span)
        else:    
            print(match)
    for match in re.finditer(reForEmail, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end, label="EMAIL ADDRESS")
        if span is not None:
            ents.append(span)
        else:    
            print(match)
    for match in re.finditer(reForEmail2, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end, label="EMAIL ADDRESS")
        if span is not None:
            ents.append(span)
    doc.ents = ents
    return (doc)

@Language.component("degree_ner")
def degree_ner(doc):
  matcher = DependencyMatcher(nlp.vocab)
  entss= list(doc.ents)
  pattern = [
    {
      "RIGHT_ID": "anchor_bachelors",       
      "RIGHT_ATTRS": {"LOWER": "bachelor"}
    },
    {
      "LEFT_ID": "anchor_bachelors",
      "REL_OP": ">",
      "RIGHT_ID": "bachelors_prep",
      "RIGHT_ATTRS": {"DEP": "prep"},
    },
    {
        "LEFT_ID": "bachelors_prep",
        "REL_OP": ">",
        "RIGHT_ID": "bachelors_object",
        "RIGHT_ATTRS": {"DEP": "pobj"},
      },
    {
        "LEFT_ID": "bachelors_object",
        "REL_OP": ".",
        "RIGHT_ID": "bachelors_prep2",
        "RIGHT_ATTRS": {"DEP": "prep"},
      },
    {
        "LEFT_ID": "bachelors_prep2",
        "REL_OP": ">",
        "RIGHT_ID": "bachelors_object2",
        "RIGHT_ATTRS": {"DEP": "pobj"},
      }
  ]
  matcher.add("Bachelors", [pattern])
  matches = matcher(doc)
  print(matches) 
  if matches:
    for match_id, token_ids in matches:
        for i in range(len(token_ids)):
            print(pattern[i]["RIGHT_ID"] + ":" + doc[token_ids[i]].text + ":", doc[token_ids[i]].idx)
        span = doc.char_span(doc[token_ids[0]].idx, doc[token_ids[-1]].idx + len(doc[token_ids[-1]].text), label="Degree1",alignment_mode="expand")
        entss.append(span)
  doc.ents = entss
  return doc

Language.component("email_phone_ner", func=email_phone_ner_fact)
Language.component("degree_ner", func=degree_ner)
