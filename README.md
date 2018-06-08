# Internship_deep_learning_project
<h2>Problem Statement and solution procedure</h2>
We have data exportSrilanka.csv,in this data attimage column is url of image and 'mymodelclassification' is classification that is expected for image but that url is sometimes irrelevant image so our task is to find out irrelevant images in thisa data for that we first need to detect object in images so for that we gonna use inception model on each image.After using this we will have a new column 'predictions' now to find out if there is relation between my classification and model classification we gonna use spacy model for word similarity and then images having similarity less than threshold are removed from dataset.

<h3>Read documentation file for understanding implementatiion of code</h3>
References : <href>https://datasciencebasicsblog.wordpress.com/computer-vision-with-deep-learning-architectures/</href>


<h3>1.Downloading inception model </h3>

will be using <b>classify_image.py</b> for this 

<h4> python  classify_image.py  model_dir='directory location'</h4>
Softwares needed in this : python2.7 <br>
packages : tensorflow,numpy,re

<h3>2.Downloading images and running model on all images in single run and storing output column in data file and running similarity model and saving in new column.</h3>

for this use <b>download_prediction_similarity.py</b>

<h4>>>> python download_prediction_similarity.py argument1 argument2</h4>

argument1 = location of csv file
argument2 = location including folder name in which images will be downloaded

software : python2.7 <br>
packages : pandas,numpy,spacy,spacy model - 'en_core_web_md'


example : >>>python download_prediction_similarity.py '/home/Desktop/exportSrilanka.csv' '/homme/Desktop/allimages' <br>

* don't forget to put location of downloaded inception model in download_prediction_similarity.py


<h4>commands to install packages</h4>

please make sure these packages are installed for python2 not python3

<h4>sudo pip install tensorflow</h4>
<h4>sudo pip install pandas </h4>
<h4>sudo pip install numpy </h4>
<h4>sudo pip install spacy</h4>
<h4>sudo pip install re</h4>
<h4>sudo python2 install spacy $ sudo python2 -m spacy download en_core_web_md  </h4>
 
