# **FastAPI project**

Demonstration using an ML model for Insurance Premium Prediction on FastAPI. 

Here is a step by step path to use the files and model.

* Create the Machine learning model of your choice and make a .pkl file to store the model.

* Here, in ML_model folder. There is the code to build base model for reference. Also there is a frontend.py file which can be used to run the modal locally in your browser with streamlit.

* There are some pydantic tutorials containg necessary details for data validation. (For tutorial purpose)

* Coming to folder Insurance_PremiumPred.

* The **model** folder contains model.pkl file and predict.py file to get predictions from the model.

* The **config** folder contains some configuration to choose cities from a list of cities to select.

* The schema folder contains app.py file which can be run using the command : uvicorn app:app --reload in the terminal.

* Once you run the command the browser pop-up can be folowed to get details and predictions.

* Can use "/", "/predict", "/health" to check API details and "/docs"(to get FASTApi swagger UI and try out predictions).



