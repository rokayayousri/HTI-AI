import streamlit as st
import pandas as pd
import joblib

st.title("Employee Attrition Prediction")

# Load the model
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    st.error("Model file 'model.pkl' not found. Please make sure it is in the same folder as this app.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.header("Enter Employee Details")
 
col1, col2 = st.columns(2)
 
with col1:
    Age = st.number_input('Age', min_value=18, max_value=60, value=36, step=1)
    BusinessTravel = st.selectbox('BusinessTravel', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
    DailyRate = st.number_input('DailyRate', min_value=102, max_value=1499, value=802, step=1)
    Department = st.selectbox('Department', ['Sales', 'Research & Development', 'Human Resources'])
    DistanceFromHome = st.number_input('DistanceFromHome', min_value=1, max_value=29, value=7, step=1)
    Education = st.number_input('Education', min_value=1, max_value=5, value=3, step=1)
    EducationField = st.selectbox('EducationField', ['Life Sciences', 'Other', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources'])
    EmployeeCount = st.number_input('EmployeeCount', min_value=1, max_value=1, value=1, step=1)
    EmployeeNumber = st.number_input('EmployeeNumber', min_value=1, max_value=2068, value=1020, step=1)
    EnvironmentSatisfaction = st.number_input('EnvironmentSatisfaction', min_value=1, max_value=4, value=3, step=1)
    Gender = st.selectbox('Gender', ['Female', 'Male'])
    HourlyRate = st.number_input('HourlyRate', min_value=30, max_value=100, value=66, step=1)
    JobInvolvement = st.number_input('JobInvolvement', min_value=1, max_value=4, value=3, step=1)
    JobLevel = st.number_input('JobLevel', min_value=1, max_value=5, value=2, step=1)
    JobRole = st.selectbox('JobRole', ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director', 'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources'])
    JobSatisfaction = st.number_input('JobSatisfaction', min_value=1, max_value=4, value=3, step=1)
    MaritalStatus = st.selectbox('MaritalStatus', ['Single', 'Married', 'Divorced'])
 
with col2:
    MonthlyIncome = st.number_input('MonthlyIncome', min_value=1009, max_value=19999, value=4919, step=1)
    MonthlyRate = st.number_input('MonthlyRate', min_value=2094, max_value=26999, value=14235, step=1)
    NumCompaniesWorked = st.number_input('NumCompaniesWorked', min_value=0, max_value=9, value=2, step=1)
    Over18 = st.selectbox('Over18', ['Y'])
    OverTime = st.selectbox('OverTime', ['Yes', 'No'])
    PercentSalaryHike = st.number_input('PercentSalaryHike', min_value=11, max_value=25, value=14, step=1)
    PerformanceRating = st.number_input('PerformanceRating', min_value=3, max_value=4, value=3, step=1)
    RelationshipSatisfaction = st.number_input('RelationshipSatisfaction', min_value=1, max_value=4, value=3, step=1)
    StandardHours = st.number_input('StandardHours', min_value=80, max_value=80, value=80, step=1)
    StockOptionLevel = st.number_input('StockOptionLevel', min_value=0, max_value=3, value=1, step=1)
    TotalWorkingYears = st.number_input('TotalWorkingYears', min_value=0, max_value=40, value=10, step=1)
    TrainingTimesLastYear = st.number_input('TrainingTimesLastYear', min_value=0, max_value=6, value=3, step=1)
    WorkLifeBalance = st.number_input('WorkLifeBalance', min_value=1, max_value=4, value=3, step=1)
    YearsAtCompany = st.number_input('YearsAtCompany', min_value=0, max_value=40, value=5, step=1)
    YearsInCurrentRole = st.number_input('YearsInCurrentRole', min_value=0, max_value=18, value=3, step=1)
    YearsSinceLastPromotion = st.number_input('YearsSinceLastPromotion', min_value=0, max_value=15, value=1, step=1)
    YearsWithCurrManager = st.number_input('YearsWithCurrManager', min_value=0, max_value=17, value=3, step=1)
 
if st.button('Predict Attrition'):
    input_data = pd.DataFrame([{
        'Age': Age,
        'BusinessTravel': BusinessTravel,
        'DailyRate': DailyRate,
        'Department': Department,
        'DistanceFromHome': DistanceFromHome,
        'Education': Education,
        'EducationField': EducationField,
        'EmployeeCount': EmployeeCount,
        'EmployeeNumber': EmployeeNumber,
        'EnvironmentSatisfaction': EnvironmentSatisfaction,
        'Gender': Gender,
        'HourlyRate': HourlyRate,
        'JobInvolvement': JobInvolvement,
        'JobLevel': JobLevel,
        'JobRole': JobRole,
        'JobSatisfaction': JobSatisfaction,
        'MaritalStatus': MaritalStatus,
        'MonthlyIncome': MonthlyIncome,
        'MonthlyRate': MonthlyRate,
        'NumCompaniesWorked': NumCompaniesWorked,
        'Over18': Over18,
        'OverTime': OverTime,
        'PercentSalaryHike': PercentSalaryHike,
        'PerformanceRating': PerformanceRating,
        'RelationshipSatisfaction': RelationshipSatisfaction,
        'StandardHours': StandardHours,
        'StockOptionLevel': StockOptionLevel,
        'TotalWorkingYears': TotalWorkingYears,
        'TrainingTimesLastYear': TrainingTimesLastYear,
        'WorkLifeBalance': WorkLifeBalance,
        'YearsAtCompany': YearsAtCompany,
        'YearsInCurrentRole': YearsInCurrentRole,
        'YearsSinceLastPromotion': YearsSinceLastPromotion,
        'YearsWithCurrManager': YearsWithCurrManager
    }])
    
    try:
        prediction = model.predict(input_data)
        if prediction[0] == 'Yes' or prediction[0] == 1:
            st.warning("The model predicts that this employee is LIKELY to leave (Attrition = Yes).")
        else:
            st.success("The model predicts that this employee is UNLIKELY to leave (Attrition = No).")
    except Exception as e:
        st.error(f"Error making prediction: {e}")

