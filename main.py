from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from src.pipeline.prediction_pipeline import CustomData,PredictionPipeline


application=Flask(__name__)

app=application

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/predictdata",methods=['GET','POST'])
def home():
    if request.method == "GET":
        return render_template("home.html")
    
    else:
         data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )
         
         df=data.get_data_as_data_frame()

         pred_pipe=PredictionPipeline()
         
         res=pred_pipe.predict(df)

         return render_template("home.html",res=res[0])


if __name__ == "__main__":
    app.run("0.0.0.0",debug=True,port=3000)

