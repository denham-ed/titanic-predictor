import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


def page_evaluation_body():

    version = 'v6'

    pipeline_dc_fe = load_pkl_file(
        f"outputs/ml_pipeline/predict-survivor/{version}/pipeline_dc_fe.pkl")
    pipeline_model = load_pkl_file(
        f"outputs/ml_pipeline/predict-survivor/{version}/pipeline_clf.pkl")
    survival_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict-survivor/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict-survivor/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict-survivor/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict-survivor/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict-survivor/{version}/y_test.csv").values

    st.header("ML Pipeline: Predict Passenger Survival")

    st.info(
        "* The pipeline was tuned aiming at least 0.80 Precision on both Survived (1) and Did Not Survive(0), "
        "since we are interested in the overall accuracy (correct predictions) to enhance the visitor experience.\n"
        "* The pipeline performance on the Train Set was 0.96 for Survived and 0.92 for Did Not Survive \n\n"
        "* The pipeline performance on the Test Set was 0.89 for Survived and 0.88 for Did Not Survive \n\n"
        "Therefore the pipeline has met the criteria for Business Requirement #2."
    )

    st.write("---")
    st.write("#### There are actually 2 ML Pipelines used in this process.")

    st.write(" * The first is responsible for data cleaning and feature engineering.")
    st.code(pipeline_dc_fe, language='python')

    st.write("* The second is for feature scaling and modelling.")
    st.code(pipeline_model, language='python')

    st.write("---")
    st.write("* The features the model was trained and their importance.")
    st.write(X_train.columns.to_list())
    st.image(survival_feat_importance)

    st.write("---")
    st.write("### Pipeline Performance")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=pipeline_model,
                    label_map=["Did Not Survive", "Survived"])

    st.write('---')

    st.caption(
        "NOTE: The scenario presented is fictional and was undertaken for the developer's "
        "Data Analytics milestone project as part of Code Institute's Diploma in Full Stack Software "
        "Development."
    )
