import streamlit as st
import pickle 
import pandas as pd


st.markdown("<h1 style='text-align: center; color: red;'>INTERNSHIP'S SUGESSTING SYSTEM</h1>", unsafe_allow_html=True)

def recommend(job):
    index = internship[internship['job_role'] == job].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:6]
    for i in distances[1:6]:
        print(internship.iloc[i[0]].job_role)

    recommended_movies = []
    for i in distances:
        recommended_movies.append(internship.iloc[i[0]].job_role)
    return recommended_movies

intern_dict = pickle.load(open('internshi.pkl' , 'rb'))
internship = pd.DataFrame(intern_dict)

similarity = pickle.load(open('similarity_intern.pkl' , 'rb'))


options = st.selectbox('WANT TO KNOW YOUR QUALIFICATION MATCHES WHICH TYPES OF OTHER INTERNSHIP PROFILE?', internship['job_role'].unique())

if st.button('Recommend'):
    recommendations = recommend(options)
    for i in recommendations:
        st.write(i)