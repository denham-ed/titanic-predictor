import streamlit as st


def page_project_hypothesis_body():

    st.header("Project Hypotheses")

    st.info(
        f"The curatorial team at SCC have put forward two hypotheses for testing during this study: \n\n"
        f"1. Male passengers were less likely to survive the tragedy than female passengers.\n\n"
        f"2. Passengers travelling in First Class were more likely to survive than passengers travelling in Third Class."
    )

    st.write(
        "Validating these hypotheses will allow SCC to examine the relationship of sex and class on survival rates."
        )
    
    st.write("---")

    st.caption(
        "NOTE: The scenario presented is fictional and was undertaken for the developer's "
        "Data Analytics milestone project as part of Code Institute's Diploma in Full Stack Software "
        "Development."
    )




