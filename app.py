from app_pages.multipage import MultiPage
from app_pages.page_survival_predictor import page_predictor_body
from app_pages.page_summary import page_summary_body
from app_pages.page_hypothesis import page_project_hypothesis_body
from app_pages.page_model_evaluation import page_evaluation_body
from app_pages.page_factors_of_survival import page_factors_of_survival_body


app = MultiPage(app_name= "Factors for Survival: Class, Sex & Age on RMS Titanic")

app.add_page("Project Summary", page_summary_body)
app.add_page("Project Hypotheses", page_project_hypothesis_body)
app.add_page("Factors for Survival Study",page_factors_of_survival_body)
app.add_page("Predict Passenger Survival", page_predictor_body)
app.add_page("Predict Passenger Survival: Model Evaluation", page_evaluation_body)
app.run() 
