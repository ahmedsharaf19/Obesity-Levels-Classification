from controller.LoadModel import LoadModel
from controller.GetFeatures import GetFeatures
from controller.GetPredection import GetPredecions

import streamlit as st

st.title('Obesity Levels Classification 👽')

Age = st.number_input('Age')
Gender = st.selectbox('Gender', ['Female', 'Male'])
Height = st.number_input('Height')
Weight = st.number_input('Weight')
CALC = st.selectbox('CALC', ['Always', 'Frequently', 'Sometimes', 'no'])
FAVC = st.selectbox('FAVC', ['no', 'yes'])
FCVC = st.number_input('FCVC')
NCP = st.number_input('NCP')
SCC = st.selectbox('SCC', ['no', 'yes'])
SMOKE = st.selectbox('SMOKE', ['no', 'yes'])
CH2O = st.number_input('CH2O')
family = st.selectbox('family_history_with_overweight', ['no', 'yes'])
FAF = st.number_input('FAF')
TUE = st.number_input('TUE')
CAEC = st.selectbox('CAEC', ['Always','Frequently','Sometimes','no'])
MTRANS = st.selectbox('MTRANS', ['Automobile','Bike','Motorbike','Public_Transportation','Walking'])

features = GetFeatures(Age, Gender, Height, Weight, CALC, FAVC, FCVC, NCP, SCC, SMOKE, CH2O, family, FAF, TUE, CAEC, MTRANS)
model = LoadModel('model.pkl')

if st.button('Predict'):
  pred = GetPredecions(model, features)
  st.write(f'Obesity Levels Is {pred}')