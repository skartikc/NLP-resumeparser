import spacy 
from spacy.language import Language
import re
# backup regex = (\+\d{0,2}\s?)?((?=1)(1?\-?\.?\s?)|)\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}
nlp = spacy.load("models\model7-202r-54r-fact\model-best")
# nlpS = spacy.load("models\model8-s-178r-78r-en-core\model-best")
# nlp = spacy.load("en_core_web_lg")

text ="""KUNAR (International Player)

Address for Correspondence:

H.No:- 33586, Main Road,

Prtap Nagar, Bathinda (Punjab)

Pin.No:- 151001

Phone no : 869**-*****

Email: adqd78@r.postjobfree.com

Profile

A dedicated and passionate leader with demonstrated success in sport, work, and education. I am goal-oriented, with strong interpersonal and creativity skills. With a positive attitude to identify winning approaches, I have the ability to accomplish objectives and lead teams to success. I posses a strong commitment to expand my knowledge and characteristics that will further my personal growth and I will apply this drive quickly to achieve positive results for a leadership company. EXPERIENCE

St. Xavier's World School Bathinda

Sports Teacher and Graphic Designer

Duration: March, 2019 to March 2021

Dr APJ Abdul Kalam Students Olympic Foundation, India and Dr B.R Ambedkar Sports Foundation, Punjab

Technical Secretary Sports

Duration: March, 2018 to till date

RESPONSIBILITY:-

I used to organise the national games, state games and takes the part as a refree.

Working in Defence Department

Duration: March, 2018 to Feb 2019

RESPONSIBILITY:-

I used trace the fraud calls and solve the public problems and I have team in which we put a raid on the illegal works. ACADEMIC BACKGROUND

Year's Qualification –

Degree / Diploma

/ Certificate

Board/University College / Institute/

University

Percentage

/ CGPA

2021 Course (AI) IEEE Students

Branvh

Nawab Shas Alam

Khan College Of E&T

90.00%

2021 Course (Cyber

Ethic)

ME&IT Govt of India Information Security

Education

Awareness

80.00%

2021 Course

(Knowledge of

Computer)

Bachelors of Engineering in Computer Science

AICTE, Ministry of

Education- Gov. Of

India

GIBS Business

School

68.00%

2017 Diploma (EE) Punjab Technical

University

Hi-Tech Polytechnic

College Bathinda

2015 10th PSEB M.H.R sen sce

School

55.00%

TECHNICAL QUALIFICATION

45 days Diploma of Automation from Infowiz, CHD.

More knowledge of Computer Software ( approved by Google) .

Power Generation Technologies (OP Jindal University )

Graphic Designer (approved by Google)

Digital Marketing (approved by Google)

Google analytics for Power User (approved by Google)

Google analytics for Beginners (approved by Google )

Front Desk Operator

Professional Sports Managements (International Olympic Committee)

Sports Coaching (International Olympic Committee)

Staellite based Navigation: A Journey from GPS to Mobile Phone Platform

(ISRO Govt of India)

AI Appreciate and AI Aware (CBSE)

Securnig Personal Data- Securnig Digital Space (Ministry of Electronics and Information Technology)

ACADEMIC / EXTRA CURRICULAR ACHIEVEMENTS

Total Professional Certificates 175, Medals 85 and Trophys 52 (Govt of India, National and International Activites)

World Book of Record IIT Chennai, India

I have 100 participation certificates of ministry Govt of India all over the India. GAMES PERFORMANCE:-

3rd Students Olympic International Games 2016-17 (Long Jump) (Gold)

International Martial Arts Taekwond Games 2017-18 (Gold)

2nd Open International Taekwondo Championship 2018 (Gold)

World Taekwondo Championship 2015-16 (Gold)

India VS Nepal Taekwondo Championship 2016 (Silver)

5th Students Olympic National Games 2018-19 (Taekwondo-Refree)

3rd Students Olympic National Gamrs 2016-17 (Bronze)

India Open Taekwondo Cup 2015 (Silver)

National Taekwondo Hanmadang 2015 (Gold)

Opne National Taekwondo Championship 2013 (Silver)

Indian Taekwondo Challenge Trophy 2015 (Gold)

1st Punjab State Students Olympic Games 2014-15 (Bronz)

16th Punjab State Taekwondo Championship 2015 (Silver)

14th Open Punjab State Taekwondo Championship 2013-14 (Gold)

1st District Stidents Olympic Games 2014-15(Gold)

1st Open District Taekwondo championship 2013-14 (Gold)

1st District Inter School Karate Cup 2015

District Taekwondo Association Bathinda (Taekwondo-Refree)

5th Students Olympic National Games 2018-19 (Long Jump) (Gold)

4th Students Olympic National Games 2017-18 (Long Jump-Refree)

1st SDCA National Games 2019 (Long Jump) (Gold)

3rd Students Olympic National Games 2016 (Long Jump) (Gold)

Students Sports Development National Games 2019 (Long Jump) (Gold)

Students Sports Development National Games 2019 (Cricket) (Gold)

Sports Development Board India (Cricket-Coach)

Students Olympic National Games (Cricket) (Gold)

2nd Summer Olympic National Games 2019 (Cricket) (Gold)

FIT India Freedom Run (Runing)

7th International Yoga Day (Ministry of AYUSH)

FIT India Freedom Run 2.0 (Ministry of Youth Affairs and Sports)

Fair Play (National Sports & Fitness Board)

International Yoga Day 2021 (Cosmos World Record)

On-Line Course on India Constitution (Department of Legal Affairs, Ministry of Low & Justice, Govt of India)

NCC, NSS AND DEFENCE :-

NCC A certificate

NCC Firing Camps

NCC Drill Camps

National Kargil War NCC Competition (22 A BN NCC-Tenali)

National NCC Competition (8 KAR BN NCC)

Indian Army NCC Unit Exam

National Service Scheme Cell (APJ Abdul Kalam Technological University NSS)

Dr. APJ Abdul Kalam E- Certificate (NSS Unit)

COVID-19 Awareness Programme (NSS Unit)

I Support Armed Forces Flag Day (Ministry of Defence)

Bangladesh Liberation War Certificate (Ministry of Defence) CERTIFICATES AND ACHIEVEMENT:

https://drive.google.com/file/d/1xDJMvZkaVjcSQ81wG 6VcZhrqekh_r_OD/view?usp=sharing

COMPUTER AND DESIGNING SOFTWARE SKILLS :

MS office

MS Excel

Power Point

Photoshop

Coral Draw

Filmora

GENERAL SKILLS :

Hard Working

Punctual

Confiden

General communication skills.

PERSONAL DETAILS :

Father’s Name : Sh. Kulwant Kumar

Date of Birth : 17 Feb 1998

Gender : Male

Marital Status : Un-married

Nationality : Indian

Languages Known : Hindi/Punjabi/English

Mobility : Willing to relocate anywhere in India and Abroad. I declare that the details above are correct and true to the best of my knowledge. Kunar(International Player)
"""
textIND = """Santosh Suresh
Mobile: +65 93897665 | https://sg.linkedin.com/in/santosh-suresh-98153440 | Email: santu22@gmail.com
PR OF E S SIO NAL S UMM A RY
 Performance-driven Banking and Operations professional with 13 years of experience in Reference data operations and core skills in
Anti-money laundering and Know your client (AML/KYC) processes
 Effective leader for driving efficiencies and process scalability
 Enthusiastic and Self driven individual with a passion to implement creative solutions and to drive changes within the organization
Skills: Anti Money Laundering, Project Management, Process Improvement, Quality assurance, Business planning, Vendor management
PR OF E S SIO NAL E X PE RI EN CE

Team Manager (Oct 2012 – Present)
Client On-boarding, Singapore
Goldman Sachs (Singapore) Pte
Reports to VP and is directly responsible for planning, reporting, vendor relationship, strategies and initiatives for Client Onboarding team.
Also, have significant exposure and working knowledge in other areas of the bank such as Static data reference operations, Periodic Review
operations and Quality assurance team.
 Responsible for managing work flow for Asia AML and KYC on-boarding team. Client On-boarding team reviews the documentation of new
clients as per compliance and regulatory requirements
 Providing oversight of the quality and productivity of work performed by the team, continually pursuing opportunities to proactively improve
efficiency and effectiveness
 Responsible for diagnosis of business problems, factoring in a seasoned understanding of the KYC/AML processes and systems in the
department
 Plan, analyze and implement initiatives/strategies for the business area ensuring that relevant objectives are achieved
 Responsible in formulation & implementation of various initiatives and on-going lead strategies for existing business units and products
 Partnering with technology teams to implement new systems and processes within the KYC/AML team to streamline process and thereby
increase efficiencies within the process
 Work with Senior management team to create annual business plans for the team locally
 Provide development opportunities and ensure that team members are adequately groomed to handle line management responsibilities, to
establish effective succession/lateral movement planning
 Champion for Operations Recruitment committee, Risk Management committee and Business Continuity Program committee for Asia
operations
 Partnering with Sales/Client relationship management team to develop innovative and faster ways to onboard clients onto the firms
platfoms
 Actively involved in client meetings along with client relations team to better understand their needs, resolve issues
 Responsible for management and delivery of the vendor team supporting the onboarding team locally
Key Accomplishments:
 Partnered with Business Architecture team to develop and implement a work flow tool for the team which helped mitigate the manual
intervention to report the progress of onboarding on a weekly basis to sales management team. Result – Mitigated the need of manual
reporting by 100%
 Streamlined the onboarding requirements by consolidating the AML requirements across client types to reduce duplication and consistency
in onboarding of clients. Result – Improved Onboarding Quality Rate year on year by 85% starting FY’2015
 Responsible for team planning, client’s requirement analysis, activity mapping and analysis, solution search and implementation. Result:
Increased Customer satisfaction by 100%, and improved employee morale and retention by 75%
 Implemented procedures on internal controls eliminating the need for steps not required in the process. Result-. Productivity increased by
100%
 Provide leadership in quality reviews, managers meeting and establish guidelines resulting in better inter-departmental communication.
 Monitor and ensure that all staff complies with Monetary Authority of Singapore, U.S. Federal Reserve and other regulatory agencies
Result: Improved overall employees’ productivity by 95%
 Played a leadership role in coordinating various activities, and conduct meetings on ACE program (Achieving Customer Excellence)
Team Leader, Periodic Review Team (Jun 2009 – Sep 2012)
Goldman Sachs International, London/Bengaluru
 Responsible for managing a 18 member Deloitte vendor team in London as a part of the Periodic Review program implementation for the
bank as a part of the Bank Holding Regulations for FY 2009 - 10
 Liaised with various federation teams such as Compliance, Legal and Credit to design and implement a process for the annual refresh
program for existing clients in the firm
 Instrumental in developing policies/procedures to adhere to regulations laid out by Federal Reserve and to be compliant for refreshing
Know Your Client processes
 Designed and collaborated a strategic path for migration of the refresh program to Bengaluru in FY2010
Key Accomplishments:
 Led the migration and knowledge transfer of the entire periodic review program from London to Bengaluru. Achieved a 100% quality rate
post migration of processes between regions
 Instrumental in setting up a Periodic Review team in Bengaluru. Responsible for 12 member team which achieved consistently 85% quality
scores for a successful 3 years of the program
 Responsible for 18 individuals reporting directly to me – 2 were promoted to the ranks of Team Leader and 1 was promoted to the rank of
a Subject Matter Expertise under my supervision
Technical Specialist - Client Onboarding (Jun 2007 – May 2009)
Goldman Sachs India Pvt Ltd – Bengaluru
 Part of the Central Accounts Group team responsible for Static data maintenance and account opening for Institutional clients of the firm
 Liaise with internal teams to assess and obtain information to open client accounts
 Responsible for training new joiners and handhold during the integration to the firm
 Engage with regional teams to support the various businesses to ensure value add to the account opening/static data maintenance
processes
 Migrated the 2nd phase of account opening functions from London to Bengaluru
Dell International Services Pvt Ltd (Nov 2002 – May 2007)
Team Manager – US/Canada Operations, Bengaluru
 Responsible for managing a strong team of 35 individuals to support the pilot batch of Operations team to support the order volumes
locally
 Responsible in formulating and implementing overall strategic and tactical goals for the operations area.
 Achieved Tell Dell people score of +80%; consistently displayed good acceptance from team members
 Initiated the Business Process Improvement (BPI) project to improve the accuracy % across Order Processing teams thereby increasing
the quality of the orders placed
 Cross-trained the team in processes like US-SMB OP, US-ESLH OP, CA Fraud & Prevention and Online Credit Card Order processing
Education
Bachelors of Commerce – Bangalore University
Post Graduate Diploma in Business Administration – Pune University
Work Authorization
Employment Pass/Work Permit – Singapore
Expiry date: October 2019
References
Available upon request"""

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

Language.component("email_phone_ner", func=email_phone_ner_fact)
nlp.add_pipe("email_phone_ner", before="ner")

print(nlp.pipe_names)

textN = text.replace("："," ")
doc = nlp(textN)
for ent in doc.ents:
    print(ent.text,ent.label_)
    
# print("--------------")
# docS = nlpS(textN)
# for ent in docS.ents:
#     print(ent.text,ent.label_)



    