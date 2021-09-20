import os
def tokenize(token):
    punc  = ['።', '::', '፣', '፡', '፤', '፨', '?', '""', '!', '{', '}', '[', ']', ',',".",")","(","፦","#","=","+","*","'","”","’","/","-","“"]
    for i in punc:
        #token = token.strip()
        token = token.replace(i,'').strip()
        
    return token
def stopword(stoplist):
    stop = open('D:/Teklay Datas/Notes/ML/Tigrinya Search engien/stopwords.txt', 'r',encoding='utf-8').read()
    stop = stop.split()
    for w in stop:
        stoplist = stoplist.replace(w,'')
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
        
    '''for i in pre:
        if len(text)>2:
            if text.startswith(i):
                text=text.replace(i,'')
    for j in suf:
        if text.endswith(j):
            text=text.replace(text[-(len(j)):-1],'')
   # pre.close()
   # suf.close()'''
    return text
doc = os.chdir('Tigrigna Corpus')
#print(doc)
stem=[]
mystr=''
name='D:/Teklay Datas/Notes/ML/Tigrinya Search engien/stemmed.txt'
for documents in os.listdir(doc):
    file = open(documents,'r',encoding="utf-8").read()
    normal = normalize(file)
    #print(normal)
    token = tokenize(normal)
    #print(token)
    stop_word = stopword(token)
    #print(stop_word)
    stemmed=stemming(stop_word)# Stemming
    #print(stemmed)
    stemmed=stemmed.replace('\n','')
    stemmed=stemmed.replace('\ufeff','')
    stem.append(stemmed)
    #print(stem)
#print(stem)
for x in stem:
    x=x.replace('   ',' ')
    x=str(x)# conver list to string
    #print(x)
    mystr=mystr+x+''
    #print(mystr)
    f=open(name,'w', encoding="utf-8")
    f.write(mystr)
    f.close()



kWF = open('D:/Teklay Datas/Notes/ML/Tigrinya Search engien/stemmed.txt','r', encoding="utf-8")
keywordFile = kWF.read()
keywordFile = keywordFile.replace('\n','')
document = keywordFile.split()
print ('Doc#',document)


def docfreq():
    dic={}
    for word in document:
        df=0
        for files in os.listdir(doc):
            f=open(files,'r',encoding='utf-8')
            read=f.read()
            ls = tokenize(read)
            ls = normalize(ls)
            ls = stopword(ls)
            ls=stemming(ls)# Stemming
            ls=ls.split()
            if word in ls:
                df=df+1
                #print (word,df)
            else:
                pass
        dic[word]=df
        #print ('dic[word]=df', dic[word],'\n')
    return dic # returns df of the vocabulary word
def invert():
    dic2={}
    for word in document:
        li=[]
        for files in os.listdir(doc):
            f=open(files,'r', encoding='utf-8')
            read=f.read()
            if word in read:
                li.append(files)
        dic2[word]=li
        #print (dic2[word])
    return dic2  # returns idf of the vocabulary word
def ndoc():
    c=0
    for files in os.listdir(doc):
        c=c+1
    return c
#print(countdf())
def colf():
    dict1={}
    for word in document:
        c=0
        for files in os.listdir(doc):
            f=open(files,'r',encoding='utf-8')
            read=f.read()
            ls = tokenize(read)
            ls = normalize(ls)
            ls = stopword(ls)
            ls=stemming(ls)# Stemming
            ls=ls.split()
            #print ls
            for i in ls:
                if (word==i):
                    c=c+1
                    #print dict1
                else:
                    continue
        else:
            pass
        dict1[word]=c
    return dict1
#print(colf())
def voc():
    voc =open('D:/Teklay Datas/Notes/ML/Tigrinya Search engien/Vocabulary File.txt','w',encoding='utf-8')
    voc.write("Term")
    voc.write('\t')
    voc.write("Df")
    voc.write('\t')
    voc.write("TF")
    voc.write('\n')
    x= docfreq()
    y=colf()
    di={}
    for a,b in x.items():
        tu={}
        for k,v in y.items():
            if a==k:
                b=str(b)
                v=str(v)
                voc.write(a)
                voc.write('\t')
                voc.write(b)
                voc.write('\t')
                voc.write(v)
                voc.write('\n')
voc()

def post():
    fi=open('D:/Teklay Datas/Notes/ML/Tigrinya Search engien/Post File.txt','w',encoding='utf-8')
    fi.write("Term")
    fi.write('\t')
    fi.write("Document#")
    fi.write('\t')
    fi.write("TF")
    fi.write('\t')
    fi.write("Location")
    fi.write('\n')

    inv=invert()
    dic={}
    for k,v in inv.items():
        doc=v
        #print k,v
        li=[]
        for y in doc:
                di={}
                di2={}
                f=open(y,'r',encoding='utf-8')
                read=f.read()
                tf=read.count(k)
                #print k
                di[y]=tf
                fi.write(k)
                fi.write('\t')
                fi.write(y)
                fi.write('\t\t')
                x=str(tf)
                fi.write(x)
                a=findLocation(read,k)
                fi.write('\t')
                fi.write(a)
                fi.write('\n')
                li.append(di)
        dic[k]=li
    return dic


def findLocation(read,word):
    read1=read.split(' ')
    dic={}
    string=''
    for w in read1:
        if word not in dic:
            found=read.find(word)
            while found > -1:
                if word not in dic:
                    dic[word]=found
                    x=str(found)
                    string=string+x
                    found=read.find(word, found+1)
                else:
                    dic[word]=str(dic[word])+" "+str(found)+" "
                    y=str(found)
                    string=string+','+y
                    found=read.find(word, found+1)
    return string
post()
