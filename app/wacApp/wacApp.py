
### Packages
import pickle
from keras_preprocessing.sequence import pad_sequences
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from  preprocessUtil import textPreprocessing
from PIL import Image
import keras
import numpy as np

### CSS
def css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

css("appeal.css")

#***************************
# Application Name
#***************************
st.markdown('<div style = "background-color: #3c4b64; text-align: center; margin: 0px 0px 10px 0px"> <h5 style = "color: white; padding: 5px;"> WAC Price Predictor  </h5> </div>', unsafe_allow_html=True)


#***************************
# Input Section: Sidebar
#***************************

### Sidebar: For input selection
st.sidebar.markdown('''<b>Enter Reason for WAC Change:</b>''', unsafe_allow_html=True)
textInput = st.sidebar.text_area('','Enter Text Here...', height=200, label_visibility = "collapsed")

st.sidebar.markdown('''<b>Enter Current WAC Price (in $):</b>''', unsafe_allow_html=True)
currentPrice = np.int64(st.sidebar.text_input('', 10))




#***************************
# Body Section: 
#***************************

if st.sidebar.button(' Get Price Prediction '):

    ### Text cleaning
    cleanedText = textPreprocessing(textInput, '').all()

    ### Creating word vector
    with open('tokenizer.pickle', 'rb') as handle:
        wordTknr = pickle.load(handle)
    tokenized_texts = wordTknr.texts_to_sequences([cleanedText])
    X = pad_sequences(tokenized_texts, maxlen=300)

    ### Loading saved model
    wacRNNModel = keras.models.load_model('cnn_model_2023-03-27_06_12_00_275007.h5')
    prediction = np.round(wacRNNModel.predict(X)[0][0],3)
    errorPrec = 0.27
    predPrice = np.round(currentPrice+currentPrice*prediction,1)

    ### Tiles
    absData = pd.DataFrame({'label': ['WAC Lb', 'WAC', 'WAC Ub'], 'value': [np.round(currentPrice+currentPrice*(prediction-prediction*errorPrec),1), predPrice, np.round(currentPrice+currentPrice*(prediction+prediction*errorPrec),1)]})
    precData = pd.DataFrame({'label': ['WAC Lb', 'WAC', 'WAC Ub'], 'value': [np.round(prediction-prediction*errorPrec,3)*100, np.round(prediction,3)*100, np.round(prediction+prediction*errorPrec,3)*100]})

    st.markdown('''<b>Predictions:</b>''', unsafe_allow_html=True)


    col1, col2 = st.columns(2)

    def addlabelsAbs(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], str(np.round(y[i],1))+'$', ha = 'center', color= 'white')

    def addlabelsPrec(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], str(np.round(y[i],1))+'%', ha = 'center', color= 'white')

   
    fig, ax = plt.subplots()
    ax.set_facecolor("#ffc107")
    ax.spines["bottom"].set_color("#ffc107")      # x axis line
    ax.spines["top"].set_color("#ffc107")
    ax.spines["left"].set_color("#ffc107")
    ax.spines["right"].set_color("#ffc107")# y axis line
    ax.tick_params(axis="x", colors="#ffc107")      # x tick labels
    ax.tick_params(axis="y", colors="#ffc107") 
    ax.bar(absData['label'], absData['value'], color ='white', edgecolor="#ffc107")
    fig.patch.set_facecolor("#ffc107")
    fig.set_figwidth(4)
    fig.set_figheight(1)
    addlabelsAbs(absData['label'], absData['value'])
    col1.markdown('''<div style = "background-color: #ffc107; color: white;padding-left: 5px;"> <span style = "background: #ffc107; color: white;"> WAC Price Prediction Range (Abs.) </span> </div>''', unsafe_allow_html=True)
    col1.pyplot(fig, use_container_width=False)


    fig, ax = plt.subplots()
    ax.set_facecolor("#df4759")
    ax.spines["bottom"].set_color("#df4759")      # x axis line
    ax.spines["top"].set_color("#df4759")
    ax.spines["left"].set_color("#df4759")
    ax.spines["right"].set_color("#df4759")# y axis line
    ax.tick_params(axis="x", colors="#df4759")      # x tick labels
    ax.tick_params(axis="y", colors="#df4759") 
    ax.bar(precData['label'], precData['value'], color ='white', edgecolor="#df4759")
    fig.patch.set_facecolor("#df4759")
    fig.set_figwidth(4)
    fig.set_figheight(1)
    addlabelsPrec(precData['label'], precData['value'])
    col2.markdown('''<div style = "background-color: #df4759; color: white;padding-left: 5px;"> <span> WAC Price Prediction Range (Prec %.) </span> </div>''', unsafe_allow_html=True)
    col2.pyplot(fig, use_container_width=False)

    ### Frequent word
    st.markdown('''<b>Key Tokens in the Text Responsible for Prediction:</b>''', unsafe_allow_html=True)

    keyTokenList = [
     'cost',
     'patient',
     'pricing',
     'market',
     'increase',
     'price',
     'product',
     'medicine',
     'factor',
     'value',
     'dynamic',
     'research',
     'investment',
     'decision',
     'regulatory',
     'access',
     'new',
     'development',
     'provided',
     'manufacturing',
     'medication',
     'condition',
     'clinical',
     'therapy',
     'inflation',
     'commercial',
     'economic',
     'approval',
     'discount',
     'support',
     'competitor',
     'particular',
     'therapeutic',
     'customer',
     'government',
     'treatment',
     'interdependent',
     'innovation',
     'category',
     'commitment',
     'invest',
     'society',
     'lifechanging',
     'fda',
     'additional',
     'formulation',
     'pharmacovigilance',
     'postmarketing',
     'improved',
     'requirement',
     'business',
     'life',
     'change',
     'approach',
     'safety',
     'conduct',
     'indication',
     'understand',
     'acquisition',
     'exelixis',
     'facility']

    helperText = textInput

    for i in textInput.split():
        if i.lower() in keyTokenList:
            helperText = helperText.replace(i, '<b style = "color: #0d6efd">'+str(i)+'</b>')

    st.markdown('''<div style = "background-color: #f8f9fa; border: 2px solid #ced4da; border-radius: 5px; padding-left: 5px; height: 150px; overflow: scroll">%s</div>'''%(helperText), unsafe_allow_html=True)

    ### Word cloud
    st.markdown('''<br>''', unsafe_allow_html=True)
    st.markdown('''<h6> Word Cloud:</h6>''', unsafe_allow_html=True)
    wordcloud = WordCloud(width = 800, height = 250,
                    background_color ='#f8f9fa',
                    stopwords = set(STOPWORDS), 
                    min_font_size = 10).generate(cleanedText)
    wordcloud.to_file('wordCloud.png')
    st.image(Image.open('wordCloud.png'))
else:
    st.info('Please enter details and press "Get Price Prediction" for recommendations')