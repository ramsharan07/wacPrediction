




**Title:** Pharmaceutical drug Wholesale Acquisition Cost (WAC) estimation using Artificial Intelligence for driving better pricing decisions
Background and Solution Overview:  Pricing a product at right price is very crucial for any business. A higher price might not attract wider customer base while a low price might lead to lower profit margins which in turn effects business’s survival. Though there are many applications of analytics for driving pricing strategies in major industries like Finance, Retail, Ecommerce etc., pharmaceutical industry has seen relatively lower adoption due to the inelastic and complex nature of drug price. Pricing decision in Pharma are majorly influenced by government policies like Medicare, Medicaid etc., coupled with multiple other complex factors. There are various levels of pricing in pharma industry based on interaction between manufacturers, wholesalers, retailers and consumers, of which Wholesale Acquisition Cost (WAC) is very vital. WAC is the cost for procuring drug by wholesales from manufactures before application of any discounts or rebates. In the current project we propose the use of historical WAC change data, submitted by manufactures to US government for price transparency, with the reason for WAC price change. The textual description on price change (Independent Variable) along with price change (Dependent Variable) can be used to train an NLP model to automatically learning difference scenarios of price change and corresponding expected change in price.

**Data Source:**
For the current work we will being using WAC price change data submitted by drug manufactures to US government which is available as opensource data in data.gov website (which is an public repository by US government for research purpose). 
Source Link: https://catalog.data.gov/dataset/prescription-drug-wholesale-acquisition-cost-wac-increases-91b27







## EDA & Model Development

**File Names:** WAC EDA and Modeling.ipynb

**Folder:** code

**Description:** WAC EDA and Modeling.ipynb has code both for data
exploration as well as model development

**Programming Language**: Python

**IDE:** Jupyter Notebook

**Packages:** Keras, Tensorflow, Pandas, Numpy and NLTK


## Web Application Development

**File Names:** wacApp.py and appeal.css

**Folder:** app/wacApp

**Description:** wacApp.py is the main file for running streamlit app
while appeal.css is for custom styling

**Programming Language**: Python, HTML, CSS

**IDE:** Visual Studio Code

**Packages:** Streamlit
