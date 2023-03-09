import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import pickle
import numpy as np
from PIL import Image
img = Image.open('place.jpg')
col1, col2, col3 = st.columns(3)
with col1:
    st.write('')
with col2:
    st.image(img, width=300, output_format='auto')
with col3:
    st.write('')
def main():
    
    html_temp="""
<style>
[data-testid="stAppViewContainer"]{
     background-color:  #36fc93 ;
   
}
.st-ae st-af st-ag st-dj st-ai st-aj st-cm st-cg st-b8{
    background-color:  #36fc93 ;
}
</style>
"""
    model = joblib.load('model_campus_placement_final.json')
    st.markdown(html_temp,unsafe_allow_html=True) 
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.markdown("*Do you want to know your placement Status???*")
    p1=st.radio("*Select Your Gender..!!*",("Male","Female"))
    if p1=="Male":
        p1=0
    elif p1=="Female":
        p1=1
    p2=st.number_input("*Secondory Education:10th Percentage*",0.0,100.00,step=1.0)
    p3=st.selectbox("*Your Secondory Board of Education-*",('Central','Others'))
    if p3=="Central":
        p3=0
    elif p3=="Others":
        p3=1
    p4=st.number_input("*Higher Secondory Education:12th Percentage*",0.0,100.00,step=1.0)
    p5=st.selectbox("*Your Higher Secondory Board of Education-*",('Central','Others'))
    if p5=="Central":
        p5=0
    elif p5=="Others":
        p5=1
    p6=st.selectbox("*Specialization in Higher Secondory Education*",('Science','Commerce','Arts'))
    if p6=="Science":
        p6=0
    elif p6=="Commerce":
        p6=1
    elif p6=="Arts":
         p6=2
    p7=st.number_input("*Degree Percentage*",0.0,100.00,step=1.0)
    p8=st.selectbox("*Under Graduation(Degree Type)-Field of Degree Education*",('Sci&Tech','Comm&Mgmt','Others'))
    if p8=="Sci&Tech":
        p8=0
    elif p8=="Comm&Mgmt":
        p8=1
    elif p8=="Others":
         p8=2
    p9=st.selectbox("*Do You Have Any Work Exprerince?*",('Yes','No'))
    if p9=="Yes":
        p9=0
    elif p9=="No":
        p9=1
    s1=st.number_input("*Enter Your Test Percentage*",0.0,100.0,step=1.0)
    p10=st.selectbox("*Branch Specialization*",('Mkt&HR','Mky&Fin'))
    if p10=="Mkt&HR":
        p10=0
    elif p10=="Mky&Fin":
        p10=1
    p11=st.number_input("*MBA Percentage*",0.0,100.00,step=1.0)
    
    new_data = pd.DataFrame({
    'gender':p1,
    'ssc_p':p2,
    'ssc_b':p3,
    'hsc_p':p4,
    'hsc_b':p5,
    'hsc_s':p6,
    'degree_p':p7,
    'degree_t':p8,
    'workex':p9,
    'etest_p':s1,
     'specialisation':p10,
    'mba_p':p11,   
},index=[0])

    if st.button("Predict"):
        pred=model.predict(new_data)
        prob=model.predict_proba(new_data)
        if pred[0]==0:
            st.warning("Sorry you can't place :disappointed_relieved:")
        else:
            st.balloons()
            st.success("You will be placed with probability of {} % ".format(np.floor(prob[0][1]*100)))
      

    
    
 

if __name__=='__main__':
    main()