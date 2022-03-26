import spacy 
from spacy.language import Language
from spacy.matcher import DependencyMatcher
import re

nlp = spacy.load("en_core_web_lg")
def remove_emojis(text):
    spl = """"#$%&()*+, -./<=>?@[\]^_{|}"""
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

def countDep(doc,dep,tokid,end):
    count = 0
    for token in doc[(tokid-4):end]:
        if str.lower(token.head.text) == "college" and token.dep_ == dep:
            count+=1
            if token.children:
                count+=sum(1 for _ in token.children)
    return count

@Language.component("email_phone_ner")
def email_phone_ner_fact(doc):
    reForEmail = r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
    reForEmail2 = r"indeed.com/r/[a-zA-Z-0-9]+/[a-zA-Z0-9-]+"
    reForNumba = r"((?=\+\d{3}\s?)\+\d{3}\s?\d{4}\s?\d{4,5}|(\(?\+\d{0,2}\)?\s?)?((?=1)(1?\-?\.?\s?)|)\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{0,4})"
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

@Language.component("college_ner")
def college_ner(doc):
  matcher = DependencyMatcher(nlp.vocab)
  entss= list(doc.ents)
  pattern6 = [
      {
          "RIGHT_ID":"anchor_college",
          "RIGHT_ATTRS":{"LOWER":"college"}
      },
      {
          "LEFT_ID":"anchor_college",
          "REL_OP":">",
          "RIGHT_ID":"appos",
          "RIGHT_ATTRS":{"DEP":"appos"}
      }
  ]
  pattern7 = [
      {
          "RIGHT_ID":"anchor_college",
          "RIGHT_ATTRS":{"LOWER":"college"}
      },
       {
          "LEFT_ID":"anchor_college",
          "REL_OP":">",
          "RIGHT_ID":"npadvmod",
          "RIGHT_ATTRS":{"DEP":"npadvmod"}
      },
  ]
  matcher.add("College", [pattern6,pattern7])
  matches = matcher(doc)
#   print(matches) 
  if matches:
    for match_id, token_ids in matches:
        # for i in range(len(token_ids)):
            # print(pattern[i]["RIGHT_ID"] + ":" + doc[token_ids[i]].text + ":", doc[token_ids[i]].idx)
        span = doc.char_span(doc[token_ids[0]-countDep(doc,"compound",token_ids[0],token_ids[-1])].idx, doc[token_ids[-1]].idx + len(doc[token_ids[-1]].text), label="COLLEGE")
        entss.append(span)
  doc.ents = entss
  return doc

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
  pattern2 = [
      {
          "RIGHT_ID":"MSC",
          "RIGHT_ATTRS":{"LOWER":"m.sc"}
      },
      {
          "LEFT_ID":"MSC",
          "REL_OP":">",
          "RIGHT_ID":"prep",
          "RIGHT_ATTRS": {"DEP": "prep"}
      },
      {
          "LEFT_ID":"prep",
          "REL_OP":">",
          "RIGHT_ID":"pobj",
          "RIGHT_ATTRS":{"DEP":"pobj"}
      }
  ]
  pattern4 = [
      {
          "RIGHT_ID":"BSC",
          "RIGHT_ATTRS":{"LOWER":"b.sc"}
      },
      {
          "LEFT_ID":"BSC",
          "REL_OP":">",
          "RIGHT_ID":"prep",
          "RIGHT_ATTRS": {"DEP": "prep"}
      },
      {
          "LEFT_ID":"prep",
          "REL_OP":">",
          "RIGHT_ID":"pobj",
          "RIGHT_ATTRS":{"DEP":"pobj"}
      }
  ]
  matcher.add("Bachelors", [pattern,pattern2,pattern4])
  matches = matcher(doc)
#   print(matches) 
  if matches:
    for match_id, token_ids in matches:
        # for i in range(len(token_ids)):
            # print(pattern[i]["RIGHT_ID"] + ":" + doc[token_ids[i]].text + ":", doc[token_ids[i]].idx)
        span = doc.char_span(doc[token_ids[0]].idx, doc[token_ids[-1]].idx + len(doc[token_ids[-1]].text), label="Degree")
        entss.append(span)
  doc.ents = entss
  return doc