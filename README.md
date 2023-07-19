# Passenger Survival Prediction - RMS Titanic Exhibition

In 1912, the RMS Titanic, the largest ship afloat at the time, set sail from Southampton, UK bound for New York, USA. Tragically, on 15 April, she sank after hitting an iceberg, resulting in the deaths of more than > 1500 passengers and crew.

The Jupyter notebooks and resulting pipeline and dashboard for this project demonstrate the collection, interrogation and presentation of data relating to passengers onboard the RMS Titanic. The scenario presented below is fictional and was undertaken for the developer's Data Analytics milestone project as part of [Code Institute's](https://codeinstitute.net/global/) Diploma in Full Stack Software Development.

## Scenario

As part of a new exhibition in Southampton, the City Council has commissioned a new study into the factors affecting the survival rate for passengers on board the Titanic.

## Dataset

- The dataset for this study is sourced from [Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset).

- It contains 891 rows representing individual passengers. The data is licensed under [CC0](https://creativecommons.org/publicdomain/zero/1.0/) and therefore is in the public domain.

- For the scenario, outlined above, we might imagine that the data is provided to the study from Southampton City Council.

- The dataset has 12 columns representing information about each passenger. The details are below:

| Variable (type)   | Meaning                                            | Range          | Notes                                          |
| ----------------- | -------------------------------------------------- | -------------- | ---------------------------------------------- |
| PassengerId (int) | An index-like unique identifier for each passenger | 1-891          |                                                |
| Survived (int)    | Marks whether the passenger survived               | 0 or 1         | 1 = Survived, 0 = Did not survive              |
| Pclass (int)      | Class of travel for passenger                      | 1-3            | 1 = First Class etc                            |
| Name (obj)        | Name of passenger                                  | n/a            | n/a                                            |
| Sex (obj)         | Sex of passenger                                   | male or female |                                                |
| Age (float)       | Age of Passenger                                   | 0.42-80        |                                                |
| SibSp (int)       | No of siblings aboard                              |                |                                                |
| Parch (int)       | No of parents/children aboad                       |                |                                                |
| Ticket (obj)      | Ticket number                                      | n/a            | Each ticket is unique                          |
| Fare (float)      | Price paid for travel                              | 0 - 512        |                                                |
| Cabin (obj)       | Cabin number                                       | n/a            |                                                |
| Embarked (obj)    | Port of embarkment                                 | C, Q or S      | C = Cherbourg, Q = Queenstown, S = Southampton |

## Business Requirements

Southampton City Council (SCC) wish to learn more about the key factors for the survival of passengers on board. They want to use this information in their new exhibition to highlight how factors such as age, sex and class (and their intersectionality) affected the outcome for passengers. They would also like to develop a tool to help visitors empathise with their imagined 1912 counterparts.

1. SCC would like to understand the patterns in the passenger data to better understand the most relevant variables correlated to survivorship.
2. SCC would like to create a tool that visitors can use to predict the likelihood of survival for a passenger that shares their demographic qualities.

## Project Hypotheses & Validation

The curatorial team at SCC have put forward two hypotheses for testing during this study:

### Hypothesis 1

Male passengers were less likely to survive the tragedy than female passengers.

### Hypothesis 2

Passengers travelling in First Class were more likely to survive than passengers travelling in Third Class.

The chi-squared test will be used to discover a relationship between survival and these variables, alongside a study with visualisations.

## Project Rationale

- **Business Requirement 1:** Data Visualisation and Correlation study

- This study will interrogate the passenger data, described above. This will allow the curatorial team to draw conclusions about the relationship between demographics and survival rate onboard.

- It will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to Survived.

- It will plot the main variables against Survived to visualise insights.

- **Business Requirement 2:** Classification Pipeline

- SCC want visitors to be able to predict the survival rate for imagined passengers. This will require a binary classification pipeline.

- SCC hopes to encourage visitors to empathise and connect with their counterparts from over a century ago. It should help to make the stories of the men, women, and children onboard more tangible and relatable

## ML Business Case

### Scope and Objective

An ML model will be used to predict if a passenger is likely to have survived the sinking of the Titanic. It will use the historical passenger data, as described above. The target variable ('Survived') is categorical and contains 2-classes. It is a supervised, 2-class, single-label classification model output: 0 (did not survive), 1 (survived).

The objective of the project is to allow SCC to elicit an empathetic response from visitors, by encouraging them to imagine themselves as passengers on the doomed vessel.

### Measuring Success

To elicit empathy from visitors and accurately represent the tragedy, the predictive tool must be accurate. SCC has set clear metrics for such success, which are:

- **80% Precision for both Survived and Did Not Survive**

### Outputs

The model will predict a likelihood of survival for individual passengers - visitors to the exhibition will be able to tweak the information provided to see how being in a different passenger class, different age or different sex would have affected the outcome.

### Heuristics

Currently, SCC does not employ any approach to predicting survival rate for hypothetical passengers.

## Dashboard Design

A Streamlit App UI will be used to present the findings of this project. It will have the following structure:

### Page 1 - Project Summary

- Context and Overview of Project
- Direct visitors to this README for more information
- Describe business requirements

### Page 2 - Project Hypotheses and Validation

- Describe project hypotheses
- Describe the results and validation process
  1.  Male passengers were less likely to survive the tragedy than female passengers
      - This is demonstrated to be true through the correlation study and visualisations.
  2.  Passengers travelling in First Class were more likely to survive than passengers travelling in Third Class.
      - This is demonstrated to be true through the correlation study and visualisations

### Page 3 - Factors for Survival Study

- Describe dataset
- Generate plots to show correlation and relationships
- State conclusions (including project hypotheses)
- Describe how it meets Business Requirement #1

### Page 4 - Predict Passenger Survival

- Set of widgets (select box and ranges) which relate to demographic qualities of passengers
- 'Predict Survival' button. This triggers the ML Pipeline and predicts whether the passenger would have survived.

### Page 5 - Predict Passenger Survival: Model Evaluation

- Considerations and conclusions after the pipeline is trained
- Present ML pipeline steps
- Feature importance
- Pipeline performance

## Acknowledgements

- The Code Institute Walkthrough Project _Churnometer_ was used as inspiration for this study and classification pipeline.
- Many of the utility functions, including Hyperparameter Optimization, are adapted from this walkthrough project.
- The support of my mentor Precious Ijege for his advice, guidance and directions to resources is gratefully acknowledged.
- Finally a huge thank you to Niel McEwen for his endless help and patience.
