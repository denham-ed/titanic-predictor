import streamlit as st
import pandas as pd
from src.data_management import load_passenger_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_survival


def page_predictor_body():

    st.header('Predicting Survival')

    st.write(
        "Visitors to the new exhibition will have the opportunity to enter their information "
        "into the predictive model and can what their fate might have been.\n"
        "This bleak exercise hopes to encourage visitors to empathise and connect with their "
        "counterparts from over a century ago. It should help to make the stories of the men, "
        "women, and children onboard more tangible and relatable.\n\n"
    )

    version = 'v6'
    pipeline_dc_fe = load_pkl_file(
        f"outputs/ml_pipeline/predict-survivor/{version}/pipeline_dc_fe.pkl")
    pipeline_model = load_pkl_file(
        f"outputs/ml_pipeline/predict-survivor/{version}/pipeline_clf.pkl")

    X_live = DrawInputsWidgets()

    if st.button("Predict Survival"):
        survivor_prediction = predict_survival(
            X_live, pipeline_dc_fe, pipeline_model)

    st.write('---')

    st.caption(
        "NOTE: The scenario presented is fictional and was undertaken for the developer's "
        "Data Analytics milestone project as part of Code Institute's Diploma in Full Stack Software "
        "Development."
    )


def DrawInputsWidgets():
    X_live = pd.DataFrame([], index=[0])
    df = load_passenger_data()

    if 'filtered_df' not in st.session_state:
        # st.session_state['Pclass'] = 1
        st.session_state['filtered_df'] = df[df["Pclass"] == 1]

    col1, col2 = st.beta_columns(2)
    col3, col4 = st.beta_columns(2)

    with col2:
        feature = "Sex"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique(),
        )
        X_live[feature] = st_widget

    with col3:
        feature = "Age"
        st_widget = st.slider(
            label=feature,
            min_value=0,
            max_value=int(df[feature].max()),
            step=1,
            value=int(df[feature].median()),
        )
        X_live[feature] = st_widget

    with col1:
        feature = "Pclass"
        st_widget = st.selectbox(
            on_change=change(df, st_widget),
            label=feature,
            options=sorted(df[feature].unique())
        )
        st.session_state['filtered_df'] = df[df["Pclass"] == st_widget]
        X_live[feature] = st_widget

    with col4:
        feature = "Fare"
        st_widget = st.slider(
            label=feature,
            min_value=float(st.session_state['filtered_df'][feature].min()),
            max_value=float(st.session_state['filtered_df'][feature].max()),
            value=float(st.session_state['filtered_df'][feature].median()),
            step=1.0,
        )
        st.write(
            f"* Most Third Class tickets cost between £7 and £15, with a median of £8\n\n"
            f"* Most Second Class tickets cost between £13 and £26, with a median of £14\n\n"
            f"* Most First Class tickets were cost between £30 and £94, with a median of £60\n\n"
        )
        X_live[feature] = st_widget  

    return X_live

def change(df, st_widget):
    st.session_state['filtered_df'] = df[df["Pclass"] == st_widget]
