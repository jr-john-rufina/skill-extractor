import json
import re
about=input('Enter about yourself:')
language=['python','java','c','c++','sql']
technology=['CNN','DL','RNN & LSTM','GNN','MLP','ANN']
skill=['AI/ML','DATA SCIENCE','DS','CAD','CLOUD COMPUTING','PROMPT ENGINEERING']
l,t,s=0,0,0
language.sort(key=len,reverse=True)
technology.sort(key=len,reverse=True)
skill.sort(key=len,reverse=True)
f_language=[]
f_tech=[]
f_skill=[]
for i in language:
    if i.lower()=='c':
        pattern = r'\bc\b(?!\+\+)'
    else:
        pattern=r'(?<!\w)'+re.escape(i)+r'(?!\w)'
    if re.search(pattern ,about,re.IGNORECASE):
        f_language.append(i)
        l=1
for i in technology:
    if  re.search(r'(?<!\w)'+re.escape(i)+r'(?!\w)',about,re.IGNORECASE):
        f_tech.append(i)
        t=1
for i in skill:
    if  re.search(r'(?<!\w)'+re.escape(i)+r'(?!\w)',about,re.IGNORECASE):
        f_skill.append(i)
        s=1
if l==0:
    print('Your language is not specified')
    ch=input('Do you want to specify your language?')
    if ch.upper()=='YES':
        lang=input('Enter your language:')
        f_language.append(lang)
if t==0:
    print('Your technology is not specified')
    ch=input('Do you want to specify your technology?')
    if ch.upper()=='YES':
        tech=input('Enter your technology:')
        f_tech.append(tech)
if s==0:
    print('Your skill is not specified')
    ch=input('Do you want to specify your skill?')
    if ch.upper()=='YES':
        skill=input('Enter your skill:')
        f_skill.append(skill)
result={
    'Languages':f_language,
    'Technologies':f_tech,
    'Skills':f_skill
    }
print(json.dumps(result,indent=4))

