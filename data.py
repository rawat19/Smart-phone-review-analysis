from operator import index
from turtle import title
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def data():
    df=pd.read_excel(r"C:\Users\Antaajack\Merged_clean_data.xlsx")
    st.title("Our Dataset")
    st.markdown(""" ## Below is a portion of our data based on the smartphone reviews of different brands and models""")
    st.dataframe(df.head(10))
def EDA():   
    st.title('Data Visualization')

    df=pd.read_excel(r"C:\Users\Antaajack\Merged_clean_data.xlsx")
    total_share=df.groupby(by="brand_y").count()
    total_share["share_percent"]=total_share.iloc[:,1]*100/len(df)  
    total_share=total_share.sort_values(by="share_percent",ascending=False).head(10)
    st.header("Market Share of Top 10 Brands")
    fig1=px.pie(total_share,values="share_percent", names=total_share.index)
    st.write(fig1)
    
    overall_rating=pd.pivot_table(df,index="brand_y",values=["overall","reviewerID"],aggfunc={"overall":"mean","reviewerID":"count"}).sort_values("reviewerID",ascending=False)
    ##overall_rating=overall_rating
    brand_options=overall_rating.index.to_list()
    st.write(overall_rating)
    st.header("Top 10 Selling Brands and their Mean Overall Score")
    brand=st.multiselect('Which brand you would like to see?',brand_options,['Samsung'])
    overall_rating=overall_rating[overall_rating.index.isin(brand)]
    
    fig2= px.bar(overall_rating,x=overall_rating.index,y="overall",color=overall_rating.index)
    ##sns.barplot(x=overall_rating.index,y=overall_rating["overall"])
    st.write(fig2)  

    review_rate=pd.pivot_table(df,index="brand_y",columns="review_sentiment",values="asin",aggfunc="count") 
    review_rate=review_rate.sort_values("POSITIVE", ascending=False)
    review_rate["total_reviews"]=review_rate.iloc[:,0]+review_rate.iloc[:,1] 
    review_rate["positive_rate"]=review_rate.iloc[:,1]*100/review_rate["total_reviews"]
    review_rate=review_rate.sort_values("total_reviews",ascending=False).head(10)
    st.header("Top Selling Brand's Positive Review Rate")
    fig3=px.bar(x=review_rate.index,y=review_rate["positive_rate"],color=review_rate.index)    
    st.write(fig3)


    
    verified_rate=pd.pivot_table(df,index="brand_y",columns="verified",values="asin",aggfunc="count") 
    verified_rate=verified_rate.sort_values(True, ascending=False)
    verified_rate["total_reviews"]=verified_rate.iloc[:,0]+verified_rate.iloc[:,1]
    verified_rate["true_rate"]=verified_rate.iloc[:,1]*100/review_rate["total_reviews"]
    verified_rate=verified_rate.sort_values("true_rate",ascending=False).head(10) 
    st.header("Top Selling Brand's Verified Review Rate")
    fig4=px.bar(x=verified_rate.index,y=verified_rate["true_rate"],color=verified_rate.index)
    st.write(fig4)
    