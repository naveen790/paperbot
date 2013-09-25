#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging

#############################################################################
## 	PaperBot- a distributed information retreival engine 		   ##
##									   ##
#############################################################################

import cgitb
import cgi 

from bs4 import BeautifulSoup
import HTMLParser
import operator
import optparse
import re
import string
import sys
import unicodedata
import urllib
import urllib2

cgitb.enable()

#print "Content-Type: text/plain;charset=utf-8"
print "Content-type:text/html\r\n\r\n"
print

form = cgi.FieldStorage()


#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging

import cgitb
import cgi 

from bs4 import BeautifulSoup
import HTMLParser
import operator
import optparse
import re
import string
import sys
import unicodedata
import urllib
import urllib2

cgitb.enable()

#print "Content-Type: text/plain;charset=utf-8"
print "Content-type:text/html\r\n\r\n"
print

form = cgi.FieldStorage()

print "<!DOCTYPE HTML>"

print "<head>"
print "<title>PAPERBOT</title>"
print "<meta name=\"description\" content=\"Naveen Natarajan Website\"/>"
print "<meta name=\"keywords\" content=\"Naveen Natarajan, Webpage and details\" />"
print "<meta http-equiv=\"content-type\" content=\"text/html; charset=windows-1252\" />"

print "<link rel=\"stylesheet\" type=\"text/css\" href=\"http://yourserver.com/cgi-bin/style.css\" />"

print "</head>"

print "<BODY>"
print "<div id=\"main\">"
print "<div id=\"header\">"
print "<div id=\"logo\">"
print "<div id=\"logo_text\">"
print "<h1>PAPERBOT</h1>"
print "</div>"
print "</div>"
print "</div>"

print "<div id=\"site_content\">"
print "<div class=\"sidebar\">"
print "<img style=\"width: 220px; height: 220px;\" alt=\"me\" src=\"paperbot.jpg\"><br>"
print "</div>"
print "<div id=\"content\">"
query = form["title"].value
query.strip()

author = form["author"].value
author.strip()

if query == "Enter Title/Keyword Here":
   query_url = ""
else:
   query_url = query.replace(" ", "+")

if author == "Enter Author Name Here":
   author_url = ""
else:
   author_url = author.replace(" ", "+")

print "<font size =\"3\" face=\"verdana\" color=\"blue\" align = \"center\"> Results for </font>"

if query_url == "" and author_url == "":
   print "ERROR!!!!!!!!! \n You should enter either the Paper Title/Keyword or the Author\n\n Both the fields are blank."
   print "<META http-equiv=\"refresh\" content=\"0;URL=http://cs.jhu.edu/~nnatara2/paper.html\">"
elif query_url != "" and author_url == "":
   print "<font size =\"3\" face=\"verdana\" color=\"blue\" align = \"center\"> query :" + query +"</font>"
   flag_weight = 1
   cite_url = 'http://citeseer.ist.psu.edu/search?q='+query_url
   ms_url = "http://academic.research.microsoft.com/Search?query="+query_url
   g_url = 'http://scholar.google.com/scholar?hl=en&q='+query_url
elif query_url == "" and author_url != "":
   print "<font size =\"3\" face=\"verdana\" color=\"blue\" align = \"center\"> author :" + author +"</font>"
   flag_weight = 2
   cite_url = 'http://citeseer.ist.psu.edu/search?q=author%3A'+author_url
   ms_url = 'http://academic.research.microsoft.com/Search?query=author%3a%28'+author_url+'%29'
   g_url = 'http://scholar.google.com/scholar?q=author%3A'+author_url
elif query_url != "" and author_url != "":
   print "<font size =\"3\" face=\"verdana\" color=\"blue\" align = \"center\">query :" + query +" and  author :" + author +"</font>"
   flag_weight = 3
   cite_url = 'http://citeseerx.ist.psu.edu/search?q=text%3A'+query_url+'+AND+author%3A'+author_url
   ms_url = "http://academic.research.microsoft.com/Search?query=author%3a%28"+author_url+"%29%20"+query_url
   g_url = 'http://scholar.google.com/scholar?as_q='+query_url+'&as_sauthors='+author_url

rank = 10

def tag_checker(tag):
    if tag.name == 'div' and str(tag.get('class')) == '[\'gs_r\']':
        return True
    return False

def _path2url(self, path):
    if path.startswith('http://'):
        return path
    if not path.startswith('/'):
        path = '/' + path
    return g_url + path

def as_int(obj):
    try:
        return int(obj)
    except ValueError:
        return None

def calculate_weight(title,auth,abstract):
    title = title.lower()
    abstract = abstract.lower()
    auth = auth.lower()
    weight = 0
    query1 = query.lower()
    author1 = author.lower()
    if flag_weight == 1:
        if(title.find(query1)) >=0:
            weight= weight + 0.8
        if(auth.find(query1))>=0:
            weight= weight + 0.2
        if(abstract.find(query1))>=0:
            weight= weight + 0.7
    elif flag_weight == 2:
        if(title.find(author1)) >=0:
            weight= weight + 0.1
        if(auth.find(author1))>=0:
            weight= weight + 0.8
        if(abstract.find(author1))>=0:
            weight= weight + 0.1
    elif flag_weight == 3:
        if(title.find(query1)) >=0:
            weight= weight + 0.8
        if(auth.find(author1))>=0:
            weight= weight + 0.7
        if(abstract.find(query1))>=0:
            weight= weight + 0.7
    return weight



cite_html_doc = urllib.urlopen(cite_url)
cite_x = cite_html_doc.readlines()
cite_title = cite_year = cite_author = cite_citations = cite_abstract = cite_linkurl = ""
cite_papers = []


ms_html_doc = urllib.urlopen(ms_url)
ms_x = ms_html_doc.readlines()
ms_title = ms_year = ms_author = ms_citations = ms_abstract = ms_linkurl = ms_weight = ""
ms_papers = []

UA = 'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.9.2.9) Gecko/20100913 Firefox/3.6.9'
req = urllib2.Request(url=g_url,headers={'User-Agent': UA})
hdl = urllib2.urlopen(req)
html_doc = hdl.read()
soup = BeautifulSoup(html_doc)
g_title = g_year = g_author = g_citations = g_abstract = g_linkurl =""
g_papers = []

flag = 0
startNum= 10
for line in ms_x:
    if "_Title" in line:
        ms_title = ms_year = ms_author = ms_citations = ms_abstract = ms_linkurl = ms_weight = ""
        ms_lineT = line.split('>')
        ms_title = ms_lineT[1].split('<')[0].replace('&#8208;','-').replace('&#58;',':').replace('&#39;','\'')
        
    if"Citations:" in line:
        ms_lineC = line.split('Citations:')[1].split('<')
        ms_citations =  ms_lineC[0].strip()
    if "http://academic.research.microsoft.com/Author" in line:
        authlist = ''
        lineA = line.split('</a><span class="span-break" >, </span>')
        for i in lineA:
            if i.find('<span class')<=0:
                lineA =  i.split('">')[-1].replace('<b>','').replace('</b>','').replace('</a>','')
                authlist = authlist+" " + lineA   
        ms_author =  authlist
    if "_Title" in line:
        ms_lineL = line.split('href=')[1].split('"')[1]
        ms_linkurl = "http://academic.research.microsoft.com/"+ms_lineL
    if "_snippet" in line:
        ms_abstract = line.split('">')[1].split('...')[0]
    if "class=\"year\"" in line:
        ms_lineY = line.split('year')[1].split('<')[0].split('>')[1].split(',')
        ms_year =  ms_lineY.pop()
        flag = 1
    if(flag):
        ms_weight = 0    
        ms_weight = calculate_weight(ms_title,ms_author,ms_abstract)
        ms_papers.append((ms_title,ms_author,ms_year,ms_abstract,ms_linkurl,ms_citations, (ms_weight*startNum)))
        flag =0
        startNum = startNum - 1

startNum= 10
for i in range(len(cite_x)):
    line = cite_x[i]
    if "doc_details" in line:
        cite_title = cite_year = cite_author = cite_citations = cite_abstract = cite_linkurl =""
        cite_link = line.split('?')[1].split('"')[0]
        cite_linkurl =  'http://citeseer.ist.psu.edu/viewdoc/summary?'+cite_link
        z= cite_x[i+1]
        cite_title = z.strip().replace('<em>','').replace('</em>','')
    if "pubyear" in line:
        cite_year = line.split('</span>')[0].split(', ')[-1] 
    if "author" in line:
        z= cite_x[i+1]
        if z.find('<link')>=0: 
            continue
        cite_author = z.strip()
    if "number of citations" in line:
        cite_citations = line.split('by ')[1].split(' ')[0]
    if "pubabstract" in line:
        z= cite_x[i+1]
        if z.find('<link')>=0: 
            continue
        cite_abstract = z.strip().replace('&lt;em&gt;','').replace('&lt;/em&gt;','')
        flag = 1
    if(flag):
        cite_weight = 0    
        cite_weight = calculate_weight(cite_title,cite_author,cite_abstract)
        cite_papers.append((cite_title,cite_author,cite_year,cite_abstract,cite_linkurl,cite_citations, (startNum*cite_weight)))
        flag =0
        startNum= startNum - 1

def parse_article(div):
    startNum= rank
    for tag in div:
        if not hasattr(tag, 'name'):
            continue
        if tag.name == 'div' and str(tag.get('class')) == '[\'gs_ri\']' and tag.a:
            g_title = HTMLParser.HTMLParser().unescape(unicodedata.normalize('NFKD', ''.join(tag.a.findAll(text=True))).encode('ascii','ignore'))
            g_linkurl = ''.join(tag.a['href'])
            g_citations = as_int(str(tag.findAll('a')).split('Cited by ')[-1].split("</a>")[0]) 
            g_author =  str(tag).split('"gs_a">')[1].split('-')[0].split(',')
            for cd in range(len(g_author)):
                ab = g_author[cd]
                if ab.find("href")>=0:
                    x = ab.split("<")[-2].split(">")[-1]
                    g_author[cd] = x
                if ab.find("<b>")>=0:
                    x = ab.replace("<b>", "").replace("</b>","")
                    g_author[cd]= x
                    ab = x
                if ab.find("&hellip;")>=0:
                    x = ab.replace("&hellip;", "")
                    g_author[cd]= x
            g_author = ''.join(g_author) 
            year = re.search(r'\b\d\d\d\d\b', str(tag))
            if ( int(year.group()) <= 2013 and  int(year.group()) > 1900):
                g_year = year.group()
            else:
                continue
            if(str(tag).find('"gs_rs">')) >= 0:
                g_abstract =  str(tag).split('"gs_rs">')[1].split('<a')[0]
                flag = 1
                if(flag):
                    g_weight = 0    
                    g_weight = calculate_weight(g_title,g_author,g_abstract)
                    g_papers.append((g_title,g_author,g_year,g_abstract,g_linkurl,g_citations, (startNum*g_weight) ))
                    flag =0
                    startNum= startNum - 1
                
for div in soup.findAll(tag_checker):
    rank = rank - 1
    parse_article(div)
            
# create a set papers
ms = 5
cite = 10
scholar = 7

all_papers= {}
papers_case= {}
for i in ms_papers:
    all_papers[i[0].lower()] = i[6]+ ms
    papers_case[i[0].lower()] = i[0]

for i in cite_papers:
    if all_papers.has_key(i[0].lower()):
        weight_prev = all_papers[i[0].lower()]
        weight_updated = weight_prev + i[6] + cite
        all_papers[i[0].lower()] = weight_updated 
    else:
        all_papers[i[0].lower()] = i[6] + cite
        papers_case[i[0].lower()] = i[0]
    
for i in g_papers:
    if all_papers.has_key(i[0].lower()):
        weight_prev = all_papers[i[0].lower()]
        weight_updated = weight_prev + i[6] + scholar
        all_papers[i[0].lower()] = weight_updated 
    else:
        all_papers[i[0].lower()] = i[6]
        papers_case[i[0].lower()] = i[0]

sorted_x = sorted(all_papers.iteritems(), key=operator.itemgetter(1))
sorted_x.reverse()

papers= {}

for i in sorted_x:
    found = 0
    tuple = []
    for j in ms_papers:
        if j[0].lower() == i[0] and found == 0:
            tuple.append((j[1], j[2], j[3], j[4], j[5],i[1]))
            papers[i[0]] = tuple
            found = 1
    for j in cite_papers:
        if j[0].lower() == i[0] and found == 0:
            tuple.append((j[1], j[2], j[3], j[4], j[5],i[1]))
            papers[i[0]] = tuple
            found = 1
    for j in g_papers:
        if j[0].lower() == i[0] and found == 0:
            tuple.append((j[1], j[2], j[3], j[4], j[5],i[1]))
            papers[i[0]] = tuple
            found = 1

# output top 10 results from dictionary  
i = 0

if len(papers_case) == 0 :
    print "<h2> No Results Found</h3><br>"
    print "<h2> Use different search terms </h3>"
    print "<META http-equiv=\"refresh\" content=\"3;URL=http://cs.jhu.edu/~nnatara2/paper.html\">"

while i < 10 and i<len(papers_case):
    paper = papers_case.get(sorted_x[i][0])
    print "<br><br>"
    link = str(papers.get(sorted_x[i][0])[0][3])
    print "<h2 ><a href=\""+ link+ "\" > "+ paper + " </a></h2>"	
    print "<font size =\"3\" face=\"verdana\" color=\"black\" align = \"center\">"
    print str(papers.get(sorted_x[i][0])[0][0])
    print "</font>"
    if len(str(papers.get(sorted_x[i][0])[0][1])) > 0:
       print ' - '
       print "<font size =\"2.5\" face=\"verdana\" color=\"black\" align = \"center\">"
       print str(papers.get(sorted_x[i][0])[0][1])
       print "</font>"
    print "<br>"
    print str(papers.get(sorted_x[i][0])[0][2]) + '...'
    print "<br>"
    if len(str(papers.get(sorted_x[i][0])[0][4])) > 0:
       print "<font size =\"2.5\" face=\"verdana\" color=\"black\" align = \"center\">"
       print "Citations:"
       print str(papers.get(sorted_x[i][0])[0][4])
       print "<br>"	
       print "</font>"
    i = i +1   

print "</div>"
print "</div>"
print "</body>"  
