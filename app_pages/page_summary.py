import streamlit as st


def page_summary_body():

    st.header("Project Overview")

    st.info(
        "In 1912, the RMS Titanic, the largest ship afloat at the time, set sail "
        "from Southampton, UK bound for New York, USA. Tragically, on 15 April, "
        "she sunk after hitting an iceberg, resulting in the deaths of more than "
        "1500 passengers and crew.\nAs part of a new exhibition in Southampton, "
        "the City Council (SCC) has commissioned a new study into the factors affecting "
        "survival rate for passengers on board the Titanic."
    )

    st.write(
        f"* For more information about this project please visit the "
        f"[Project README file](https://github.com/denham-ed/titanic-predictor) in the project's GitHub repo.")

    st.success(
        "The project has 2 business requirements:\n\n"
        "1. SCC would like to understand the patterns in the passenger "
        "data to better understand the most relevant variables correlated to a survivorship.\n\n"
        "2. SCC would like to create a tool that visitors can use to predict the likelihood of "
        "survival for a passenger that share their demographic qualities."
    )

    st.write('---')

    st.caption(
        "NOTE: The scenario presented is fictional and was undertaken for the developer's "
        "Data Analytics milestone project as part of Code Institute's Diploma in Full Stack Software "
        "Development."
    )
