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

def text_pp(text):
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
    return text1

# backup regex = (\+\d{0,2}\s?)?((?=1)(1?\-?\.?\s?)|)\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}
nlp = spacy.load("en_core_web_lg")
# nlpS = spacy.load("models\model8-s-178r-78r-en-core\model-best")
# nlp = spacy.load("en_core_web_lg")

text ="""RESUME
WONG KIM FUNG, PENNY (王劍烽)
Tel : 6335 5368
Email : penny_and1@hotmail.com
WORKING EXPERIENCE
02/2017-07/2017 Financial accountant for AP & GL, Chanel Hong Kong Limited (6 months contract)
• Handle daily accounting operations: invoices checking, payment and prepare journal.
• Work with GL team on month-end closing (Balance sheet reconciliation & Bank Reconciliation)
• Assist on Inter-company invoice settlement process

03/2015 to 02/2017 Senior accounts clerk, Richemont Asia Pacific Limited
11/2012 to 03/2015 Accounts clerk, Richemont Asia Pacific Limited
• Handled daily accounting operations: invoices checking, payment and prepare journal.
• Liaised with other departments on solving issues of AP accounting entries, payment and
purchase order queries.
• Reviewed Purchase Order.
• Performed stock count with inventory team and inventory audit with auditor in HK and Macau.
• Prepared monthly reports and schedules to the management.
• Provided SAP training to new joiners in the Group and Masions, e.g. purchase order creation and
vendor maintenance.
• Assisted the SAP project team for the launch of the SAP VIM project in Shanghai.
09/2011 to 08/2012 Accounting clerk, VF Hong Kong Limited (MNC)
• Proceeded payment requests from brands and supporting departments
• Prepared a JV and maintained the up-to-date AP database in SAP system
• Liaised with internal parties for various payment requests and invoice checking
• Answered finance-related enquiry from internal customer.
04/2010 to 06/2011 Accounting officer, ChunWo Vegetable Company
• Audited client testing reports and maintained master database accuracy
• Conducted analytical reports, Powerpoint and summaries for management
• Answered telephone enquiry and assisted in sample checking
• Provided general clerical support to the team, e.g. filing and data entry
08/2009 to 02/2010 Teleservices executive officer, PCCW Blackberry hotline
• Provided Blackberry technical supports to end customers
• Handled customer enquiries on billing issue
• To assist customers in checking data usage data
EDUCATION
09/2017- BA(Hons) Accounting, Edinburgh Napier University, Scoop City University of Hong Kong
09/2007-07/2009 Hong Kong Community College, Hong Kong Polytechnic University
Associate Degree - China Business
09/1999-07/2007 Cognitio College (Kowloon)
Form 1 – Form 7
QUALIFICATIONS
2007 Hong Kong Advanced Level Examinations
2005 Hong Kong Certificate Education of Examination
KEY EXPERIENCE
• Strong interpersonal skills with clients, staff and management,
• Self-driven and supportive to the work, able to work under pressure
• Enthusiastic team player but able to work well as an individual
• Highly motivated to learn and attention to details in the workplace
2
COMPUTER / TYPING SKILLS
• MS Office (Word, Excel, Power Point)
• SAP accounting system
Current salary: $21000 x 13 months
Expected salary: $23,000 per month
Availability: Immediate"""

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

@Language.component("name_ner")
def name_ner(doc):
    idx = []
    min = 1000000
    for tok in doc[0:17]:
        if tok.pos_ == "PROPN":
            idx.append(tok.i)
            if(tok.i<min):
                min = tok.i
    final = min
    for tok in doc[min+1:min+5]:
        if tok.pos_ == "PROPN":
            final = final +1
        else:
            break
    print("min = " + str(min))
    print("final = " + str(final))
    return doc



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
Language.component("name_ner", func=name_ner)
nlp.add_pipe("name_ner", before="email_phone_ner")

print(nlp.pipe_names)

doc = nlp(text_pp(text))
# print(doc.text)
# for ent in doc.ents:
#     print(ent.text,ent.label_)
for tok in doc:
    print(tok.text + tok.pos_)
# doc1 = nlp(text1.lower())
# for ent in doc1.ents:
#     print(ent.text,ent.label_)
    
# print("--------------")
# docS = nlpS(textN)
# for ent in docS.ents:
#     print(ent.text,ent.label_)



    