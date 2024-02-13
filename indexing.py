#-------------------------------------------------------------------------
# AUTHOR: Kevin Hoang
# FILENAME: indexing.py
# SPECIFICATION: Reading a file and returning a document-term matrix
# FOR: CS 4250- Assignment #1
# TIME SPENT: Around 3-4 hrs, 2/3 on assignment and 1 on code
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal. Hint: use a set to define your stopwords.
stopWords = {"I","and","She","her","They","their"} #Filtering

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
stemming = {"cats":"cat", "dogs":"dog", "loves":"love"} #Dictionary to compare words and creating stemming
 
#Identifying the index terms.
terms = []
for document in documents:
    words = document.split()    #Separting documents
    temp =[]
    for word in words:
        if word not in stopWords:   #Filtering out words using stopWords and stemming 
            stemmed = stemming.get(word,word)
            temp.append(stemmed)
    terms.append(temp)
            
#Building the document-term matrix by using the tf-idf weights.
d1LoveCount = 0
d1CatCount = 0
d1DogCount = 0
d1Total = 0

d2LoveCount = 0
d2CatCount = 0
d2DogCount = 0
d2Total = 0

d3LoveCount = 0
d3CatCount = 0
d3DogCount = 0
d3Total = 0

loveDCount = 0 
dogDCount = 0
catDCount = 0

for words in terms:
    if "cat" in words:      #Getting D value
        catDCount+=1
    if "dog" in words:
        dogDCount+=1
    if "love" in words:
        loveDCount+=1

for words in terms[0]:      #Finding Values for tf/idf/tf-idf calculations
    if words == "love":
        d1LoveCount+=1
        d1Total+=1
    if words == "dog":
        d1DogCount+=1
        d1Total+=1
    if words == "cat":
        d1CatCount+=1
        d1Total+=1
        
for words in terms[1]:
    if words == "love":
        d2LoveCount+=1
        d2Total+=1
    if words == "dog":
        d2DogCount+=1
        d2Total+=1
    if words == "cat":
        d2CatCount+=1
        d2Total+=1
        
for words in terms[2]:
    if words == "love":
        d3LoveCount+=1
        d3Total+=1
    if words == "dog":
        d3DogCount+=1
        d3Total+=1
    if words == "cat":
        d3CatCount+=1
        d3Total+=1
        
tfLove1 = d1LoveCount / d1Total     #tf calculations
tfLove2 = d2LoveCount / d2Total
tfLove3 = d3LoveCount / d3Total

tfCat1 = d1CatCount / d1Total
tfCat2 = d2CatCount / d2Total
tfCat3 = d3CatCount / d3Total

tfDog1 = d1DogCount / d1Total
tfDog2 = d2DogCount / d2Total
tfDog3 = d3DogCount / d3Total

idfLove = math.log10(len(terms)/loveDCount)            #idf calculations
idfCat = math.log10(len(terms)/catDCount)
idfDog = math.log10(len(terms)/dogDCount)

tfidfLove1 = tfLove1 * idfLove          #tf-idf calculations
tfidfCat1 = tfCat1 * idfCat
tfidfDog1 = tfDog1 * idfDog

tfidfLove2 = tfLove2 * idfLove
tfidfCat2 = tfCat2 * idfCat
tfidfDog2 = tfDog2 * idfDog

tfidfLove3 = tfLove3 * idfLove
tfidfCat3 = tfCat3 * idfCat
tfidfDog3 = tfDog3 * idfDog

row1 = [round(tfidfLove1,2), round(tfidfDog1,2), round(tfidfCat1,2)]
row2 = [round(tfidfLove2,2), round(tfidfDog2,2), round(tfidfCat2,2)]
row3 = [round(tfidfLove3,2), round(tfidfDog3,2), round(tfidfCat3,2)]
        
        
docTermMatrix = []

docTermMatrix.append(row1)
docTermMatrix.append(row2)
docTermMatrix.append(row3)

#Printing the document-term matrix.
for row in docTermMatrix:
    print(row)
