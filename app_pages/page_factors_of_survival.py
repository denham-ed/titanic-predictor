import streamlit as st
from src.data_management import load_passenger_data
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from feature_engine.discretisation import EqualFrequencyDiscretiser
import plotly.graph_objects as go

sns.set_style('whitegrid')

def page_factors_of_survival_body():
    st.header("Factors of Survival")

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
        f"the variables in the transaction data are correlated to Surival for passengers. \n\n"
        f"The most correlated variables are: \n"
        f"* Sex\n"
        f"* Pclass\n"
        f"* Fare\n"
        f'* Embarked\n'
    )

    vars_to_study = ['Sex', 'Pclass', 'Fare','Embarked']    

    df_eda = df.filter(vars_to_study + ['Survived'])
    df_eda['Pclass'] = df_eda['Pclass'].map({1: '1st Class', 2: '2nd Class', 3:'3rd Class'})
    df_parallel = prepare_parallel_plot(df_eda)
 
    if st.checkbox("View Survival Levels per Variable"):
        survival_level_per_variable(df_eda, vars_to_study)

    if st.checkbox("View Parallel Plot"):
        st.info(
            "This parallel plot indicates a connection the highest fares and survival rate, "
            "as well as highlighting the relationship between Sex and Pclass."
        )
   
        show_parallel_plot(df_parallel)


    st.subheader("Conclusions")

    st.success(
    "The study and visualisations above support the following conclusions: \n\n"
    "1. There is a significant relationship between Sex and survival rate. \n\n"
    "* Female passengers were more likely to survive than Male passengers. \n\n"
    "2. There is a significant relationship between Pclass and surival rate. \n\n"
    "* Passengers travelling in First Class were more likely to survive than passengers "
    "travelling in 3rd class."
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
    sns.countplot(data=df, x=col, hue=target_var, order=df[col].value_counts().index)
    plt.xticks(rotation=45)
    plt.title(f"{col}", fontsize=20, y=1.05)
    plt.savefig(f"outputs/plots/{col}-against-survival.png")
    st.image(f"outputs/plots/{col}-against-survival.png")


def plot_numerical(df, col, target_var):
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)
    plt.savefig(f"outputs/plots/{col}-against-survival.png")
    st.image(f"outputs/plots/{col}-against-survival.png")


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
    import plotly.express as px
    fig = px.parallel_categories(df_parallel, color="Survived")
    st.plotly_chart(fig)




