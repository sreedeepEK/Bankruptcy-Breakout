import pickle
import streamlit as st

model_path = "D:/Data Science/ExcelR project/Bankruptcy_prevention_project/bankruptcy_model.sav"
model = pickle.load(open(model_path, 'rb'))

st.title('Bankruptcy Prediction using ML')
col1, col2, col3 = st.columns(3)
with col1:
    industrial_risk = st.text_input("Industrial Risk")

with col2:
    management_risk = st.text_input("Management Risk")

with col3:
    financial_flexibility = st.text_input("Financial Flexibility")

with col1:
    credibility = st.text_input("Credibility")

with col2:
    competitiveness = st.text_input("Competitiveness")

with col3:
    operating_risk = st.text_input("Operating Risk")

#Predicting the output
model_output = ''
if st.button('Print result'):
    prediction = model.predict([[industrial_risk, management_risk, financial_flexibility, credibility, competitiveness,	operating_risk]])
    if prediction[0] == 0:
        model_output = "The model suggests a low likelihood of bankruptcy."
    else:
        model_output = "The model suggests a high likelihood of bankruptcy."
    st.success(model_output)