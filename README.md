# Survival Prediction - Titanic Exhibition

In 1912, the RMS Titanic, the largest ship afloat at the time, set sail from Southampton, UK bound for New York, USA. Tragically, on 15 April, she sunk after hitting an iceberg, resulting in the deaths of more than > 1500 passengers and crew.

The Jupyter notebooks and resulting pipeline and dashboard for this project demonstrate the collection, interrogation and presentation of data relating to passengers onboard the RMS Titanic. The scenario presented below is fictional and was undertaken for the developer's Data Analytics milestone project as part of [Code Institute's](https://codeinstitute.net/global/) Diploma in Full Stack Software Development.

  

## Scenario

As part of a new exhibition in Southampton, the City Council has commissioned a new study in to the factors affecting survival rate for passengers on board the Titanic.

  

## Dataset

  

- The dataset for this study is sourced from [Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset).

- It contains 891 rows representing individual passengers. The data is licensed under [CC0](https://creativecommons.org/publicdomain/zero/1.0/) and therefore is in the public domain.

- For the purposes of the scenario, outlined above, we might imagine that the data is provided to the study from Southampton City Council.

- The dataset has 12 columns representing information about each passenger. The details are below:

  

| Variable (type) | Meaning | Range | Notes |

| -------------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |



  

## Business Requirements

Southampton City Council (SCC) wish to learn more about the key factors for survival for passengers on board. They want to use this information in their new exhibition in order to highlight the ways in which factors such as age, sex and class (and their intersectionality) affected the outcome for passengers. They would also like to develop a tool to help visitors empathise with their imagined 1912 counterparts.

1. SCC would like to understand the patterns in the passenger data to better understand the most relevant variables correlated to a survivorship.

2. SCC would like to create a tool that visitors can use to predict the likelihood of survival for a passenger that share their demographic qualities.

## Project Hypotheses & Validation

 
The curatorial team at SCC have put forward two hypotheses for testing during this study:

### Hypothesis 1

Male passengers were less likely to survive the tragedy than female passengers.

### Hypothesis 2

Passengers travelling in First Class were more likely to survive than passengers travelling in Third Class.

The chi-squared test will be used to validate both of these hypotheses.

## Project Rationale

  

## Make this more user story focussed.

  

-  **Business Requirement 1:** Data Visualisation and Correlation study

- This study will interrogate the passenger data, described above.

- It will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to Survived.

- It will plot the main variables against Survived to visualise insights.

-  **Business Requirement 2:** Classification Pipeline

- SCC want visitors to be able to predict the survival rate for imagined passengers. This will require a binary classification pipeline.

  

## ML Business Case

  

### Scope and Objective


A ML model will be used to predict if a passenger is likely to have survived the sinking of the Titanic. It will use the historical passenger data, as described above. The target variable ('Survived') is categorical and contains 2-classes. It is a supervised, 2-class, single-label classification model output: 0 (did not survive), 1 (survived).

 
The objective of the project is to allow SCC to elicit an empathetic response from visitors, by encouraging them to imagine themselves as passengers on the doomed vessel.



### Measuring Success

 
In order to elicit empathy from visitors and accurately represent the tragedy, the predictive tool must be accurate. SCC have set clear metrics of such success, which are:

-  **90% Recall & Precision for Survived.** 


### Outputs

  

The model output is defined as a flag, indicating if a transaction and _the associated probability of fraud!?!!??!!!?!?._

*For this proof of concept, individual transactions will be entered into the dashboard. In future these will be able to be done in bulk*

  

### Heuristics

Currently SCC does not employ any approach to predicting survival rate for hypothetical passengers.

  

### Describe training data...