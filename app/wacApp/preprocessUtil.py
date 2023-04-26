
from wordcloud import WordCloud, STOPWORDS
import re
from nltk.stem import WordNetLemmatizer

class textPreprocessing():
    '''
    Class takes text as input and return processed text post all data cleaning steps
    '''
    def __init__(self, text, dgName):
        self.procText = text
        self.drugName = dgName
       
    ## Module for text normalization
    def textNormalization(self):
        self.procText = self.procText.lower()
        
    ## Module for removing unwanted spaces
    def stripSpaces(self):
        self.procText = self.procText.strip()
    
    ## Module for stopwords removal
    def stopwordRemoval(self):
        self.procText = ' '.join([i for i in self.procText.split(' ') if i not in STOPWORDS])
        
    ## Module for removing special characters
    def specialCharRemoval(self):
       # specialWords = ['.', ',', "'", '?', '-', '_', '+', '$', '®', '™', '(', ')']
        
        self.procText = ' '.join([re.sub("[^A-Z]", "", i,0,re.IGNORECASE) for i in self.procText.split(' ')])
        #for i in specialWords:
            #self.procText = re.sub(''+i, '', self.procText)
            
            
              
            
    ## Module for drug names from text
    def drugNameRemoval(self):
        #print(str(self.drugName).split(' ')[0].lower())
        #print(self.procText.replace(str(self.drugName).split(' ')[0].lower(), ''))
        self.procText = ' '.join(self.procText.replace(str(self.drugName).split(' ')[0].lower(), '').split(' '))
    
    ## Module for wordLemmatization
    def rootExtLemmatization(self):
        self.procText = ' '.join([WordNetLemmatizer().lemmatize(i) for i in self.procText.split(' ')])
    
    ## Module for call all preprocessing steps
    def all(self):
        self.textNormalization()

        self.stopwordRemoval()
        self.specialCharRemoval()
        self.drugNameRemoval()
        self.rootExtLemmatization()
        self.stripSpaces()
        return self.procText
                                   
