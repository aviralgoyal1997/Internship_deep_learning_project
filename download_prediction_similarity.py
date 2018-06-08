import pandas as pd
import numpy as np
import urllib
import os 
import glob
import csv
import sys

input_path = sys.argv[1]

image_path = sys.argv[2]
if not os.path.exists(image_path):
    os.makedirs(image_path)

#downloading all images from links
df=pd.read_csv('%s'% input_path) #directory of input file
a=df['attImage']
i=0
while(i<len(a)):
    try:
        urllib.urlretrieve(a[i], "%s/%s.jpg"% (image_path,i))
        i=i+1
    except:
        continue


#running model on all images and storing result in names.csv

filenames=glob.glob(image_path+"/*.jpg")
s=[]
with open('names.csv','w') as csvfile:   #result will be written in this file
          
     fieldnames=['name','prediction']
     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
     writer.writeheader()
     for f in filenames:
         try:
             writer.writerow({'name':'%s'% f,'prediction': (str(os.popen('python classify_image.py --model_dir='location of directory in which model is installed' --image %s'% f).readlines()).split('(',1)[0].strip("['"))})
         except:
                continue

#result.csv file having input csv file with predictions column attached    
df1=pd.read_csv('names.csv')
df['predictions']=df1['prediction']
df.to_csv('result.csv')


#for finding similarities between model predictions and given classifications

import spacy
import pandas as pd
import numpy as np


nlp = spacy.load('en_core_web_md') 

df=pd.read_csv('result.csv') 

expected=df['MyModelClassifications']

predicted_classification=df['new_classification']

q=0
m=[]
while (q<len(expected)):
    m.append(nlp(u'%s' %  predicted_classification[q]))
    q=q+1
predicted_classification=m
i=0
expected_classification=[]
while (i<len(expected)):
    expected_classification.append(expected[i].split("/")[-1])
    i=i+1
tr=df.MyModelClassifications.unique()
i=0
n=[]
while (i<len(tr)):
    n.append(tr[i].split("/")[-1])
    i=i+1
t=np.array(n)
t[t=='sacredreligioussites']='relegious'
t[t=='sightslandmarks']='landmark'
t[t=='pointsofinterestlandmarks']='landmark'
t[t=='buddhisttemples']='temple'
t[t=='bodiesofwater']='water'
t[t=='natureparks']='park'
t[t=='historicalplace']='place'
t[t=='fungames']='game'
t[t=='sportscomplexes']='complex'
t[t=='touristattraction']='tourist'
t[t=='monumentsstatues']='statue'
t[t=='specialitymuseums']='museum'
t[t=='placeofworship']='worship'
t[t=='churchescathedrals']='church'
t[t=='nationalpark']='park'
t[t=='historymuseums']='museum'
t[t=='historicsites']='site'
t[t=='catholiccathedral']='cathedral'
t[t=='shoppingmalls']='mall'
t[t=='shoppingmall']='mall'
t[t=='hindutemple']='temple'
t[t=='shoppingcomplex']='complex'
t[t=='anglicanchurch']='church'
t[t=='conferencecenter']='center'
t[t=='lighthouses']='house'
t[t=='lighthouse']='house'
t[t=='trussbridge']='bridge'
t[t=='observationdeck']='deck'
t[t=='railstation']='station'
t[t=='casinosgambling']='casino'
t[t=='corporateoffice']='office'
t[t=='clothingstore']='cloth'
t[t=='departmentstores']='store'
t[t=='concertsshows']='concert'
t[t=='artgallery']='gallery'
t[t=='outdooractivities']='outdoor'
t[t=='sportscampsclinics']='clinic'
t[t=='classesworkshops']='workshop'
t[t=='swimclub']='club'
t[t=='culturalcenter']='center'
t[t=='buildingcomplex']='complex'
t[t=='architecturalbuildings']='building'
t[t=='performingartstheater']='theater'
t[t=='observationdeckstowers']='tower'
t[t=='governmentbuildings']='building'
t[t=='governmentoffice']='office'
t[t=='fleastreetmarketss']='market'
t[t=='floatingmarket']='market'
t[t=='presbyterianchurch']='church'
t[t=='militarymuseums']='museum'
t[t=='religiousorganisation']='organisation'
t[t=='thudugalaellawaterfall']='waterfall'
t[t=='artmuseums']='museum'
t[t=='catholicchurch']='church'
t[t=='historicallandmark']='landmark'
t[t=='jewelrystore']='jewelry'
t[t=='fleastreetmarkets']='market'

sw=pd.Series(expected_classification)
sw=pd.Series(expected_classification)

t[t=='sacredreligioussites']='relegious'
t[t=='sightslandmarks']='landmark'
t[t=='pointsofinterestlandmarks']='landmark'
t[t=='buddhisttemples']='temple'
t[t=='bodiesofwater']='water'
t[t=='natureparks']='park'
t[t=='historicalplace']='place'
t[t=='fungames']='game'
t[t=='sportscomplexes']='complex'
t[t=='touristattraction']='tourist'
t[t=='monumentsstatues']='statue'
t[t=='specialitymuseums']='museum'
t[t=='placeofworship']='worship'
t[t=='churchescathedrals']='church'
t[t=='nationalpark']='park'
t[t=='historymuseums']='museum'
t[t=='historicsites']='site'
t[t=='catholiccathedral']='cathedral'
t[t=='shoppingmalls']='mall'
t[t=='shoppingmall']='mall'
t[t=='hindutemple']='temple'
t[t=='shoppingcomplex']='complex'
t[t=='anglicanchurch']='church'
t[t=='conferencecenter']='center'
t[t=='lighthouses']='house'
t[t=='lighthouse']='house'
t[t=='trussbridge']='bridge'
t[t=='observationdeck']='deck'
t[t=='railstation']='station'
t[t=='casinosgambling']='casino'
t[t=='corporateoffice']='office'
t[t=='clothingstore']='cloth'
t[t=='departmentstores']='store'
t[t=='concertsshows']='concert'
t[t=='artgallery']='gallery'
t[t=='outdooractivities']='outdoor'
t[t=='sportscampsclinics']='clinic'
t[t=='classesworkshops']='workshop'
t[t=='swimclub']='club'
t[t=='culturalcenter']='center'
t[t=='buildingcomplex']='complex'
t[t=='architecturalbuildings']='building'
t[t=='performingartstheater']='theater'
t[t=='observationdeckstowers']='tower'
t[t=='governmentbuildings']='building'
t[t=='governmentoffice']='office'
t[t=='fleastreetmarketss']='market'
t[t=='floatingmarket']='market'
t[t=='presbyterianchurch']='church'
t[t=='militarymuseums']='museum'
t[t=='religiousorganisation']='organisation'
t[t=='thudugalaellawaterfall']='waterfall'
t[t=='artmuseums']='museum'
t[t=='catholicchurch']='church'
t[t=='historicallandmark']='landmark'
t[t=='jewelrystore']='jewelry'
t[t=='fleastreetmarkets']='market'

expected_classification=t
i=0
o=[]
while (i<len(expected)):
    o.append(nlp(u'%s' %  expected_classification[i]))
    i=i+1
j=0
similarity_values=[]
while (j<len(expected)):
       similarity_values.append(o[j].similarity(predicted_classification[j]))
       j=j+1

simil=pd.Series(similarity_values)
df['similarity']=simil

df.to_csv('data_with_similarity.csv') #in exportSrilanka data now we have new column similarity
























