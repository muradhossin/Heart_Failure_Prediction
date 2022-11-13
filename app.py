import pickle
import streamlit as st


#Loading th saved model

heart_model = pickle.load(open("heart_model.sav", 'rb'))

st.title("Heart Disease Prediction using Machine Learning")

genderList = ['Select gender',0,1]
ChestPainTypeList = ['Select ChestPainType', 0, 1,2,3]
heartdiseaseList = ['Select heart disease', 0, 1]
RestingECGList = ['Select RestingECG', 0, 1,2]
ExerciseAnginaList = ["Select ExerciseAngina", 0,1]
STSlopeList = ['Select ST_Slope', 0, 1,2]
FastingBSList = ['Select FastingBS', 0, 1,]


Age = st.slider('Age', min_value= 1, max_value= 110, step=1, value= 20)
Sex = st.selectbox("Sex [ 0 = Male, 1 = Female ]", genderList)
ChestPainType = st.selectbox("ChestPainType [ 0 = Asymptomatic, 1 = Non-Anginal Pain, 2 = Atypical Angina, 3 = Typical Angina, ]", ChestPainTypeList)
RestingBP = st.slider("RestingBP ", min_value= 0, max_value= 200, step=1, value= 100)
Cholesterol = st.slider("Cholesterol ", min_value= 0, max_value= 603, step=1, value= 200)
FastingBS = st.selectbox('FastingBS [ 0 = otherwise, 1 = if FastingBS > 120 mg/dl ]', FastingBSList)
RestingECG = st.selectbox('RestingECG [ 0 = Normal, 1 = showing probable, 2 = abnormality ,]', RestingECGList)
MaxHR = st.slider('MaxHR', min_value= 60, max_value= 202, step=1, value= 100)
ExerciseAngina = st.selectbox("ExerciseAngina [ 0 = No, 1 = Yes ]", ExerciseAnginaList)
Oldpeak = st.slider("Oldpeak", min_value= -2.6, max_value= 6.2, step=0.01, value=0.0)
ST_Slope = st.selectbox('ST_Slope [ 0 = flat, 1 = upsloping, 2 = downsloping,]', STSlopeList)


#code for prediction
heart_diagnosis = ''

#creating a button for prediction

if st.button('Check your result'):
    heart_predict = heart_model.predict([
        [
            Age,
            Sex,
            ChestPainType,
            RestingBP,
            Cholesterol,
            FastingBS,
            RestingECG,
            MaxHR,
            ExerciseAngina,
            Oldpeak,
            ST_Slope,
        ]
        ])
    
    if (heart_predict[0] == 1):
        heart_diagnosis = 'the patient had a heart disease'

    else:
        heart_diagnosis = 'the patient had not a heart disease'

st.success(heart_diagnosis)
