import bibtexparser

with open("my_papers.bib") as bibtex_file:
  bibtex_str=bibtex_file.read()
bibdb=bibtexparser.loads(bibtex_str)

df={'title':[],'doi':[],'volume':[],'pages':[],'author':[],'year':[],'journal':[]}



for i in bibdb.entries:
  for k in df.keys():
    if k in i.keys():
      df[k].append(i[k])
    else:
      df[k].append("")

import pandas as pd
df=pd.DataFrame(df)
df=df.sort_values("year",ascending=False)

def fix_title(s):
  return s.replace("{","").replace("}","").replace(r"\textendash","-").replace("~"," ").replace(r"$\textbackslashmathrm\Si\_\29\$","Si29")

def fix_pages(s):
  return str(s).split('-')[0]

def fix_authors(s):
  alist=s.split(" and ")
  retstr=""
  for i,a in enumerate(alist):
    print(a)
    spl=a.split(",")
    retstr+=spl[1]+" "+ spl[0]
    if i < len(alist)-1:
      retstr+=","

  return retstr.replace("{","").replace("}","")
    

df['title']=[fix_title(x) for x in df['title']]
df['pages']=[fix_pages(x) for x in df['pages']]
df['author']=[fix_authors(x) for x in df['author']]

print(df)

with open("papers.md",'w') as f:
  f.write("""---
layout: page
title: Papers
---
""")
  for row in df.iterrows():
    r=row[1]
    f.write( "<i>"+r['title']+"</i>  <br>" \
        + r['author'] +" <br>"\
        + r['journal'] +" "+\
        "<b>"+r['volume']+"</b> "+\
        r['pages'] + \
        " ("+r['year']+") " + 
        "[DOI](https://doi.org/"+r['doi']+")\n\n")

