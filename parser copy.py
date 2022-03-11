import spacy 
from spacy.language import Language
from spacy.matcher import DependencyMatcher
import re

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

# backup regex = (\+\d{0,2}\s?)?((?=1)(1?\-?\.?\s?)|)\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}
nlp = spacy.load("models\parser-try\model-best")
# nlpS = spacy.load("models\model8-s-178r-78r-en-core\model-best")
# nlp = spacy.load("en_core_web_lg")

text ="""Savita Sharma
• Cellular Number: (+65) 83832851 • Email Address: savita_86@hotmail.com
PROFESSIONAL WORK EXPERIENCE
March 2010 – Present KPMG (Singapore)
Asst Manager (Forensic Advisory)
■ Manage a team of transaction monitoring analysts. Performed Quality
Assurance Review to ensure high quality standard review of transactions.
Perform AML controls and ongoing review of transactions flagged by the
monitoring system; investigate and close out the alerts thoroughly in a timely
manner, and ensuring significant issues identified are fully investigated and
promptly escalated where necessary.
■ Managed compliance team of an international private bank to perform quality
check on annual and trigger event account reviews of customer due diligence
files. Risk assessment of existing customers via risk assessment matrix and
detecting gaps in the CDD files. Ensured remediation and transaction
monitoring of selected red flags.
■ Managed engagement in Wholesale Banking Division of a US bank for the
quality review and remediation of KYC. Achieved full compliance status,
meeting the bank’s new AML global policy standard. Client types varied from
fund, foreign correspondent bank to corporate. Conducted internal training on
compliance to ensure staff development and knowledge management.
■ Manage engagement in a private bank, scope included performing adverse
news screening on highlighted accounts, including the discounting of false
positives and escalation of true matches to the bank’s AML compliance
department. This was pursuant to the designation of tax crimes as predicate
money laundering offences in Singapore.
■ Reviewed and assessed the impact of FATCA on asset management by
conducting FATCA entity impact assessment that analyses and proposes the
likely FATCA entity classification and the obligations and impact under the
various respective classifications.
■ Managed an engagement in global bank in an investigation into allegations of
irregular SIBOR and SOR rate setting activities which involved reviewing and
analyzing communications evidence and offshore/onshore irregular trading
activities.
■ Forensic review into financial affairs of MNC with operations in Australia, New
Zealand, Hong Kong, China and Singapore, and is also part of an international
group located in the UK, Europe, Middle East and South Africa. The
investigation involved examining a wide number of significant transactions.
■ Performed statutory financial statement audit for listed companies.
Responsibilities as an audit engagement member include review of internal
control, client interview and identification of key areas of improvements, perusal
of accounting records and assistance in preparation of financial statements.
■ Awarded Service Excellence Awards by KPMG for outstanding performance
EDUCATION
Association of Certified Anti-Money Laundering Specialist (ACAMS)
 Expected Completion Date : Dec 2016
Association of Chartered Certified Accountants (ACCA)
St. Stephen's College, Delhi
 Association of Chartered Certified Accountants graduate Jun 07 – Dec 09
Institute of Singapore Chartered Accountants (ISCA)
 Chartered Accountant graduate Jun 07 – Dec 09
University of London
 M.Sc in Professional Accountancy
 Expected Completion Date: Jun 2017
Oxford Brookes University
 B.Sc (Hons) in Applied Accounting 
Jun 07 – Dec 09
 Upper Second Class graduate
IT/IS SKILLS
 Microsoft Office Suites (Access, Excel, Frontpage, Powerpoint and Words)
 CAAT softwares (Computer-Assisted Audit Technique softwares, e.g IDEA, Monetary Unit Sampling, etc
 ACCPAC
 Others: SPSS, MSOFT, QUICKBOOK
 e-Audit, e discovery, Sampling / fraud detection softwares
 Lexis Nexis, World Check, Cosima, Factiva
. Bachelor of Arts in Modern Art.


PROFESIONAL BODY MEMBERSHIP
 Association of Chartered Certified Accountants (ACCA)
 Institute of Singapore Chartered Accountants (ISCA)
 Association of Certified Anti-Money Laundering Specialist (ACAMS)
REREFENCES
 Available upon request
EXPECTED SALARY
 Market Rate/ per company policy (negotiable)
"""

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

Language.component("email_phone_ner", func=email_phone_ner_fact)
nlp.add_pipe("email_phone_ner", before="ner")
Language.component("degree_ner", func=degree_ner)
nlp.add_pipe("degree_ner", before="ner")
Language.component("college_ner", func=college_ner)
nlp.add_pipe("college_ner", before="ner")

print(nlp.pipe_names)

textN = text.replace("："," ").replace("\n\n\n","\n\n").replace("\n\n",". ").replace("\n",". ").replace("..",".")
insensitive_hippo = re.compile(re.escape('bachelors'), re.IGNORECASE)
textN2 = insensitive_hippo.sub('Bachelor',textN)
insensitive_hippo = re.compile(re.escape('msc'), re.IGNORECASE)
textN2 = insensitive_hippo.sub('M.Sc',textN)
insensitive_hippo = re.compile(re.escape('bsc'), re.IGNORECASE)
textN2 = insensitive_hippo.sub('B.Sc',textN)
text1 = textN2.replace("\n"," ").replace("$"," ").replace("\\n",' ')
text1 = remove_white(text1)
text1 = remove_emojis(text1)
doc = nlp(text1)
for ent in doc.ents:
    print(ent.text,ent.label_)
# spacy.displacy.serve(doc1, style="dep")
# doc1 = nlp(text1.lower())
# for ent in doc1.ents:
#     print(ent.text,ent.label_)
    
# print("--------------")
# docS = nlpS(textN)
# for ent in docS.ents:
#     print(ent.text,ent.label_)



    