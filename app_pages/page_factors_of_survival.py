import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import pandas as pd
from src.data_management import load_passenger_data
from scipy.stats import chi2_contingency
from feature_engine.discretisation import EqualFrequencyDiscretiser


sns.set_style('whitegrid')


def page_factors_of_survival_body():
    st.header("Factors for Survival Study")

    df = load_passenger_data()

    st.info(
        "Southampton City Council (SCC) wish to learn more about "
        "the key factors for survival for passengers on board. They "
        "want to use this information in their new exhibition in order "
        "to highlight the ways in which factors such as age, sex and class "
        "(and their intersectionality) affected the outcome for passengers."
    )

    if st.checkbox("Inspect Passenger Data"):
        st.write(
            f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns.\n\n"
            f"The first 10, used to give an indication of the format of the data, are below.")

        st.write(df.head(10))

    st.write("---")

    st.subheader("Correlation Study")

    st.write(
        f"A correlation study was conducted using Jupyter notebooks to better understand how "
        f"the variables in the transaction data are correlated to Survival for passengers. \n\n"
        f"The most correlated variables are, according to the initial study are: \n"
        f"* Sex\n"
        f"* Pclass\n"
        f"* Fare\n"
    )

    vars_to_study = ['Sex', 'Pclass', 'Fare']

    df_eda = df.filter(vars_to_study + ['Survived'])
    df_eda['Pclass'] = df_eda['Pclass'].map(
        {1: '1st Class', 2: '2nd Class', 3: '3rd Class'})
    df_parallel = prepare_parallel_plot(df_eda)

    if st.checkbox("View Survival Levels per Variable"):
        survival_level_per_variable(df_eda, vars_to_study)
        st.info(
            "The following observations are clear from the plots: \n\n"
            "* Male passengers appear to be less likely to survive than female passengers. \n"
            "* Passengers in Third Class were very likely not to survive. In First Class, "
            "passengers were more likely to survive than not."
            "* As Fare decreases, passengers become less likely to survive."
        )

    if st.checkbox("View Parallel Plot"):
        show_parallel_plot(df_parallel)
        st.info(
            "This parallel plot indicates a connection the highest fares and survival rate, "
            "as well as highlighting the relationship between Sex and Pclass."
        )

    st.write("---")

    st.subheader("Hypothesis Testing")

    if st.checkbox("Hypothesis 1: Male passengers were less likely to survive the tragedy than female passengers."):
        plot_expected_surival_by_sex(df)

    if st.checkbox("Hypothesis 2: Passengers travelling in First Class were more likely to survive than passengers travelling in Third Class."):
        plot_expected_surival_by_class(df)

    st.subheader("Conclusions")

    st.success(
        "The study and visualisations above support the following conclusions: \n\n"
        "1. There is a significant relationship between Sex and survival rate. \n\n"
        "* Female passengers were more likely to survive than Male passengers. \n\n"
        "2. There is a significant relationship between Pclass and surival rate. \n\n"
        "* Passengers travelling in First Class were more likely to survive than passengers "
        "travelling in 3rd class.\n\n"
        "The conclusions of this study meet Business Requirement #1."
    )

    st.write("---")

    st.caption(
        "NOTE: The scenario presented is fictional and was undertaken for the developer's "
        "Data Analytics milestone project as part of Code Institute's Diploma in Full Stack Software "
        "Development."
    )

    # Utility Functions


def plot_categorical(df, col, target_var):
    plt.figure(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var,
                  order=df[col].value_counts().index)
    plt.xticks(rotation=45)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(plt)


def plot_numerical(df, col, target_var):
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(plt)


def survival_level_per_variable(df_eda, vars_to_study):
    target_var = 'Survived'
    for col in vars_to_study:
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
            print("\n\n")
        else:
            plot_numerical(df_eda, col, target_var)
            print("\n\n")


def prepare_parallel_plot(df_eda):
    n_classes = 10
    disc = EqualFrequencyDiscretiser(q=n_classes, variables=['Fare'])
    df_parallel = disc.fit_transform(df_eda)
    classes_ranges = disc.binner_dict_['Fare'][1:-1]
    fare_map = {}
    for n in range(0, n_classes):
        if n == 0:
            fare_map[n] = f"<{round(classes_ranges[0],2)}"
        elif n == n_classes-1:
            fare_map[n] = f"+{round(classes_ranges[-1],2)}"
        else:
            fare_map[n] = f"{round(classes_ranges[n-1],2)} to {round(classes_ranges[n],2)}"

    df_parallel['Fare'] = df_parallel['Fare'].replace(fare_map)
    return df_parallel


def show_parallel_plot(df_parallel):
    fig = px.parallel_categories(df_parallel, color="Survived")
    st.plotly_chart(fig)


def plot_expected_surival_by_sex(df):
    contingency_table = pd.crosstab(df['Survived'], df['Sex'])
    chi2, p_value, dof, expected = chi2_contingency(contingency_table)
    contingency_table.index = ['Did Not Survive', 'Survived']
    contingency_table.columns = ['Female', 'Male']
    expected_df = pd.DataFrame(
        expected, index=['Did Not Survive', 'Survived'], columns=['Female', 'Male'])
    st.write(
        "Below is the expected surival rate by sex, if sex had no relationship to surival.")
    st.table(expected_df.round().astype(int))
    st.write("Here is the actual surival rate by sex.")
    st.table(contingency_table)
    st.write(
        "There is a statistically significant relationship between 'Survived' and 'Sex'."
        "It looks like male passengers were disproportionately less likely to survive "
        "compared to female passengers.")

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    for i, sex in enumerate(contingency_table.columns):
        ax[i].pie(contingency_table[sex], labels=contingency_table.index,
                  autopct='%1.1f%%', startangle=90)
        ax[i].set_title(f'Survival Status - {sex}')

    st.pyplot(fig)
    st.info(
        "The pie charts again above highlight the disparity in outcomes between the male and female passengers."
    )

def plot_expected_surival_by_class(df):
    contingency_table = pd.crosstab(df['Survived'], df['Pclass'])
    chi2, p_value, dof, expected = chi2_contingency(contingency_table)
    contingency_table.index = ['Did Not Survive', 'Survived']
    contingency_table.columns = ['First Class', 'Second Class', "Third Class"]
    expected_df = pd.DataFrame(
        expected, index=['Did Not Survive', 'Survived'], columns=['First Class', 'Second Class', "Third Class"])
    st.write(
        "Below is the expected survival rate by class, if class had no relationship to survival.")
    st.table(expected_df.round().astype(int))
    st.write("Here is the actual survival rate by class.")
    st.table(contingency_table)
    st.write(
        "There is a statistically significant relationship between 'Survived' and 'Class'."
        "It looks like First Class passengers were disproportionately more likely to survive "
        "compared to Third Class passengers.")

    fig, ax = plt.subplots(1, 3, figsize=(10, 5))
    
    for i, pclass in enumerate(contingency_table.columns):
        ax[i].pie(contingency_table[pclass], labels=contingency_table.index, autopct='%1.1f%%', startangle=90)
        ax[i].set_title(f'Survival Status By Class - {pclass}')

    st.pyplot(fig)
    st.info(
        "The pie charts again above highlight the disparity in outcomes between passengers across the class categories."
    )
