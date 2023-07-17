import streamlit as st

def predict_survival(X_live, pipeline_dc_fe, pipeline_model):
    X_live_survival_dc_fe = pipeline_dc_fe.transform(X_live)
    survival_prediction = pipeline_model.predict(X_live_survival_dc_fe)
    survival_prediction_proba = pipeline_model.predict_proba(X_live_survival_dc_fe)

    survival_prob = survival_prediction_proba[0,survival_prediction][0] * 100
    if survival_prediction == 1:
        survival_result = 'would have'
    else:
        survival_result = 'would not have'

    statement = (
        f'### There is {survival_prob.round(1)}% probability '
        f'that this passenger **{survival_result} survived**.')

    st.write(statement)

    return survival_prediction
