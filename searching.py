import os
import math
def tokenize(token):
    punc  = ['።', '::', '፣', '፡', '፤', '፨', '？','?', '""', '!', '{', '}', '[', ']', ',',".",")","(","፦","#","=","+","*","'","”","’","/","-","“"]
    for i in punc:
        token = token.replace(i,'')
        token = token.strip()
    return token
def stopword(stoplist):
    stop = open('D:/Teklay Datas/Notes/ML/Tigrinya Search engien/stopwords.txt', 'r',encoding='utf-8').read()
    stop = stop.split()
    for w in stop:
        stoplist = stoplist.replace(w,"")
        #print(s_w)
    return stoplist
    stop.close()
def normalize(norm):
    h1 = ['ሀ','ሁ','ሂ','ሃ','ሄ','ህ','ሆ']
    h2 = ['ኀ','ኁ','ኂ','ኃ','ኄ','ኅ','ኆ']
    s1 = ['ሰ','ሱ','ሲ','ሳ','ሴ','ስ','ሶ']
    s2 = ['ሠ','ሡ','ሢ','ሣ','ሤ','ሥ','ሦ']
    ts1 = ['ፀ','ፁ','ፂ','ፃ','ፄ','ፅ','ፆ']
    ts2 = ['ጸ','ጹ','ጺ','ጻ','ጼ','ጽ','ጾ']
    for i in range(len(h1)):
        norm = norm.replace(h2[i], h1[i])
        norm = norm.replace(s2[i], s1[i])
        norm = norm.replace(ts2[i], ts1[i])
    return norm

def stemming(text):
    pre = open('D:/Teklay Datas/Notes/ML/Tigrinya Search engien/prefix.txt','r', encoding='utf-8').read()
    pre = pre.split()
    suf = open('D:/Teklay Datas/Notes/ML/Tigrinya Search engien/sufix.txt','r', encoding='utf-8').read()
    suf = suf.split()

    for n in range(0,len(text)):
        for i in range(0,len(pre)-1):
            if(len(text)>2):
                if(text.startswith(pre[i])):
                    text=tex.replace(pre[i],'')
                    i=len(pre)
        for j in range(0,len(suf)-1):
            if(len(text)>2):
                if(text.endswith(suf[j])):
                    text=text.replace(suf[j],'')
                    j=len(suf)
    return text
doc = os.chdir('Tigrigna Corpus')
#string=''
#stem=[]
#mystr=''
query =input('ኣልሽ:')
while query =='':
    query =input('በይዘኦም/ኣን ሕቶኦም ብትክክል ይፅሓፉ:')
q=open('D:/Teklay Datas/Notes/ML/Tigrinya Search engien/query.txt','w',encoding='utf-8')
q.write(query)
q.close()
def wordfreq(files):
    #print (files)
    dict0={}
    f=open(files,'r',encoding="utf-8")
    wordList=f.read()
    wordList=wordList.split()
    wordfreq = [wordList.count(p) for p in wordList]
    dictionary = dict(zip(wordList, wordfreq))
    count2 = 0
    for t in wordList:
        count2+=1
    dict0[files]=count2
    return dict0[files] 

def ndoc():
    c=0
    for files in os.listdir(doc):
        c=c+1
    return c
def tfidf():
    N=ndoc()
    v=open('D:/Teklay Datas/Notes/ML/Tigrinya Search engien/Vocabulary File.txt','r',encoding='utf-8')
    v=v.readlines()
    del v[0]
    #print(v)
    p=open('D:/Teklay Datas/Notes/ML/Tigrinya Search engien/Post File.txt','r',encoding='utf-8')
    p=p.readlines()
    del p[0]
    #print(p)
    #Sp=p[1:]
    dic={}
    for y in p:
        zz=y.split()
            #print(zz)
        term2=zz[0]
        doc=zz[1]
        tf=zz[2]
        for x in v:
            z=x.split()
            #print(z)
            df=z[1]
            term1=z[0]
            st=''
            if term1==term2:
                doc=zz[1]
                wf=wordfreq(doc)
                tf1=float(tf)
                tf1=tf1/wf
                dfi=float(df)
                df1=N/(dfi+0.000000001)
                p=math.log(df1,2)
                idf=tf1*p
                st=doc+' '+term2
                dic[st]=idf
                #print(dic[st])
    return dic
search=open('D:/Teklay Datas/Notes/ML/Tigrinya Search engien/query.txt','r', encoding='utf-8').read()
print(search)
search = tokenize(search)
search = normalize(search)
search = stopword(search)
search=stemming(search)# Stemming
search=search.split()
ff=open('D:/Teklay Datas/Notes/ML/Tigrinya Search engien/Vocabulary File.txt','r',encoding='utf-8').read()
read=ff.split()
#if search !='':
def docfreq_query():
        dic={}
        dic2={}
        for word in search:
            df=0
            li=[]
            for files in os.listdir(doc):
                f=open(files,'r',encoding='utf-8').read()
                if word in f:
                    df=df+1
                    dic[word]=df
        return dic,df,word# returns df of the vocabulary word
x,y,z=docfreq_query()
#print()
d={}
tf=1
NN=ndoc()
if y!=0:
    fl=float(NN)/float(y)
    idf=math.log(fl,2)
    we=0.5+0.5*tf
    w=we*idf
    d[z]=w
#else:
#    print ("ይቅሬታ  ዝተረከበ መረዳእታ የለን")

weight=tfidf()
query=d
#print(query)
sim={}
for key in query:
    for docword in weight:
        if key in docword:
            sim[docword]=query[key]*weight[docword]
x= sim
dicc={}
for s,v in x.items():
    qo=s.split()
    a=qo[0]
    dicc[a]=v
d=dicc
items = [(v, k) for k, v in d.items()]
items.sort()
items.reverse() # so largest is first
items = [(k, v) for v, k in items]
i=1
print('ብመሰረት ቃላ መሕተት ዝተረከቡ ጠቀምቲ ፋይላት እዞም ዝስዕቡ እዮም')
print('<><><><><><><><><><><><><><><>')
print('Rank\t\tSim. \t\t \t\tDoc#')
for x in items:
    print (i,'.\t',x[1],'------------>\t', x[0])
    i=i+1
for y in items:
    i= input ("እቲ ፋይል ንምክፋት ትሕዝቶ ቁፅሪ የእትው：")
    y=y[0]
    z=open(y,'r',encoding='utf-8').read()
    print(z)
    
    
